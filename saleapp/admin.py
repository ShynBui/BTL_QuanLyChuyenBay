import cloudinary.uploader

from saleapp.models import UserRole
from saleapp import app, db, untils
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from flask import request, redirect, jsonify
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

admin.add_view(LogoutView(name='Logout'))
admin.add_view(ChatAdmin(name='ChatAdmin'))