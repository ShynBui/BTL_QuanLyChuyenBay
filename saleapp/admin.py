from decimal import Decimal
from gettext import gettext

import cloudinary.uploader
from flask_admin.form import FormOpts
from flask_admin.helpers import get_redirect_target
from flask_admin.model.helpers import get_mdict_item_or_list
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField
from wtforms.validators import InputRequired, Length

from saleapp.models import UserRole, Flight_AirportMedium, Flight, PriceOfFlight, PlaneTicket
from saleapp import app, db, untils
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import request, redirect, jsonify, flash
from datetime import datetime


class AuthenticatedModelView(ModelView):
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
        total = Decimal(0)
        airline_name = request.args.get('airline_name')
        date = request.args.get('month')
        statistics = untils.statistic_revenue_follow_month(airline_name=airline_name,
                                                          date=date)
        for s in statistics:
            if s[1]:
                total = total + s[1]
        return self.render('admin/index.html',statistics=statistics, total=total)


admin = Admin(app=app, name='QUẢN TRỊ MÁY BAY', template_mode='bootstrap4',
              index_view=MyAdminIndex())

class ModelView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    # edit_modal = True
    page_size = 10
    column_filters = ['id']
    column_searchable_list = ['id']

class FlightManagementView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    # edit_modal = True
    page_size = 10
    column_filters = ['id']
    column_searchable_list = ['id']
    form_excluded_columns = ['airportMediums', 'tickets', 'prices']
    column_labels = {
        'id': 'Mã chuyến bay',
        'departing_at': 'Thời gian khởi hành',
        'arriving_at': 'Thời gian đến'
    }

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

        return self.render("admin/flight-details.html",
                           model=model,
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
admin.add_view(Flight_Airportedium_View(Flight_AirportMedium, db.session, name='Trạm dừng', endpoint='stops'))
admin.add_view(PriceView(PriceOfFlight, db.session, name='Quản lý giá', endpoint='prices'))
admin.add_view(TicketView(PlaneTicket, db.session, name='Quản lý vé', endpoint='tickets'))
admin.add_view(ChatAdmin(name='ChatAdmin'))
admin.add_view(LogoutView(name='Logout'))