from gettext import gettext

import cloudinary.uploader
from flask_admin.helpers import get_redirect_target
from flask_admin.model.helpers import get_mdict_item_or_list
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, SelectField
from wtforms.validators import InputRequired, Length

from saleapp.models import UserRole, Flight_AirportMedium, Flight, Airplane, Airline
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
        return self.render('admin/index.html')


admin = Admin(app=app, name='QUẢN TRỊ MÁY BAY', template_mode='bootstrap4',
              index_view=MyAdminIndex())


class FlightForm(FlaskForm):
    id = StringField(name="id", validators=[InputRequired(), Length(max=10)])
    name = StringField(name="name", validators=[InputRequired(), Length(max=50)])
    departing_at = DateTimeLocalField(name="departing_at", format="%Y-%m-%dT%H:%M",
                                      validators=[InputRequired()])
    arriving_at = DateTimeLocalField(name="arriving_at", format="%Y-%m-%dT%H:%M",
                                     validators=[InputRequired()])
    planes = SelectField('planes', choices=[])
    airlines = SelectField('airlines', choices=[])

class FlightManagementView(AuthenticatedModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    # edit_modal = True
    page_size = 10
    column_filters = ['id']
    column_searchable_list = ['id']
    column_labels = {
        'id': 'Mã chuyến bay',
        'departing_at': 'Thời gian khởi hành',
        'arriving_at': 'Thời gian đến'
    }

admin.add_view(LogoutView(name='Logout'))
admin.add_view(FlightManagementView(Flight, db.session, name='Quản lý chuyến bay', endpoint='flights'))
admin.add_view(ChatAdmin(name='ChatAdmin'))