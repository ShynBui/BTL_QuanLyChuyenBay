from datetime import datetime
from gettext import gettext
from math import ceil

from flask_admin.helpers import get_redirect_target
from flask_admin.model.helpers import get_mdict_item_or_list
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField, FloatField
from wtforms.validators import InputRequired, Length

from saleapp.models import UserRole, Flight_AirportMedium, Flight, PriceOfFlight, PlaneTicket, Airline, Airport, Airplane, Rank
from saleapp import app, db, untils
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import request, redirect, flash


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

class ChatAdmin(BaseView):
    @expose('/')
    def index(self):

        room = untils.get_unreply_room()
        # print(room)

        return self.render('admin/chat_admin.html', room=room, user=untils.get_user_by_id(current_user.id))

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class MyAdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


admin = Admin(app=app, name='QUẢN TRỊ MÁY BAY', template_mode='bootstrap4',
              index_view=MyAdminIndex())

class StatsView(AuthenticatedView):
    @expose('/')
    def index(self):
        total = 0.0
        airline_name = request.args.get('airline_name')
        date = request.args.get('month')
        statistics = untils.statistic_revenue_follow_month(airline_name=airline_name,
                                                           date=date)
        for s in statistics:
            if s[1]:
                total = total + s[1]
        return self.render('admin/statistic.html', statistics=statistics, total=total)

class ModelView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    # edit_modal = True
    page_size = 10
    column_filters = ['id']
    column_searchable_list = ['id']


class FlightForm(FlaskForm):
    departing_at = DateTimeLocalField(name="departing_at", format="%Y-%m-%dT%H:%M",
                                      validators=[InputRequired()])
    arriving_at = DateTimeLocalField(name="arriving_at", format="%Y-%m-%dT%H:%M",
                                     validators=[InputRequired()])
    planes = SelectField('planes', choices=[])
    airlines = SelectField('airlines', choices=[])
    rank = SelectField('ranks', choices=[])
    money = FloatField('money', validators=[InputRequired()])

    stop_time_begin = DateTimeLocalField(name="stop_time_begin", format="%Y-%m-%dT%H:%M")
    stop_time_finish = DateTimeLocalField(name="stop_time_finish", format="%Y-%m-%dT%H:%M")

    description = StringField(name="description")
    airport = SelectField('airports', choices=[])


class FlightManagementView(ModelView):
    form_excluded_columns = ['airportMediums', 'tickets', 'prices']
    column_labels = {
        'id': 'Mã chuyến bay',
        'departing_at': 'Thời gian khởi hành',
        'arriving_at': 'Thời gian đến'
    }

    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        return_url = get_redirect_target() or self.get_url('.index_view')

        if not self.can_create:
            return redirect(return_url)

        sts_msg = ''
        am_msg = ''
        form = FlightForm()

        form.planes.choices = [p.id for p in Airplane.query.all()]
        form.airlines.choices = [a for a in Airline.query.all()]
        form.rank.choices = [r.name for r in Rank.query.all()]
        form.airport.choices = [ap.name for ap in Airport.query.all()]

        if request.method == "POST":
            departing_at = form.departing_at.data
            arriving_at = form.arriving_at.data
            plane = form.planes.data
            airline = form.airlines.data
            rank = form.rank.data
            money = form.money.data
            stb = form.stop_time_begin.data
            stf = form.stop_time_finish.data
            des = form.description.data
            ap = form.airport.data

            sts_msg = untils.check_flight(departing_at, arriving_at, plane)

            if sts_msg == 'success':
                try:
                    untils.save_flight(departing_at, arriving_at, plane, airline)
                    f = db.session.query(Flight).order_by(Flight.id.desc()).first()
                    untils.save_price(rank, f.id, money)
                except:
                    sts_msg = 'Đã có lỗi xảy ra khi lưu chuyến bay! Vui lòng quay lại sau!'

                if stb and stf:
                    am_msg = untils.check_stop_station(stb,stf, airline, ap, f.id)
                    if am_msg == 'success':
                        # try:
                        untils.save_airport_medium(stb, stf, des, f.id, ap)
                        # except:
                        #     untils.del_flight(f.id)
                        #     am_msg = 'Đã có lỗi xảy ra khi lưu sân bay trung gian! Vui lòng quay lại sau!'
                    else:
                        untils.del_flight(f.id)
                        am_msg = am_msg

        return self.render('admin/create.html', form=form,
                           sts_msg=sts_msg, am_msg=am_msg, return_url=return_url)

    @expose('/details/')
    def details_view(self):
        return_url = get_redirect_target() or self.get_url('.index_view')

        if not self.can_view_details:
            return redirect(return_url)

        id = get_mdict_item_or_list(request.args, 'id')
        if id is None:
            return redirect(return_url)

        model = self.get_one(id)

        if model is None:
            flash(gettext('Record does not exist.'), 'error')
            return redirect(return_url)

        apm_list = Flight_AirportMedium.query.filter(
            Flight_AirportMedium.flight_id.__eq__(id)
        ).all()

        price = PriceOfFlight.query.filter(PriceOfFlight.flight_id.__eq__(id))

        return self.render("admin/flight-details.html",
                           model=model, price=price,
                           details_columns=self._details_columns,
                           get_value=self.get_detail_value,
                           apm_list=apm_list,
                           return_url=return_url)

class Flight_Airportedium_View(ModelView):
    column_labels = {
        'id': 'Mã trạm dừng',
        'stop_time_begin': 'Thời gian bắt đầu dừng',
        'stop_time_finish': 'Thời gian tiếp tục bay',
        'description': 'Mô tả'
    }

class PriceView(ModelView):
    column_labels = {
        'id': 'Mã giá',
        'price': 'Giá'
    }

class TicketView(ModelView):
    column_labels = {
        'id': 'Mã vé',
        'subTotal': 'Tổng tiền'
    }

admin.add_view(FlightManagementView(Flight, db.session, name='Quản lý chuyến bay', endpoint='flights'))
admin.add_view(Flight_Airportedium_View(Flight_AirportMedium, db.session, name='Quản lý trạm dừng', endpoint='stops'))
admin.add_view(TicketView(PriceOfFlight, db.session, name='Quản lý giá', endpoint='prices'))
admin.add_view(TicketView(PlaneTicket, db.session, name='Quản lý vé', endpoint='tickets'))
admin.add_view(ChatAdmin(name='ChatAdmin'))
admin.add_view(StatsView(name='Thống kê'))
admin.add_view(LogoutView(name='Logout'))