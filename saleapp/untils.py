from saleapp.models import User, UserRole
from flask_login import current_user
from sqlalchemy import func, and_
from saleapp import app, db
import json
import hashlib
from sqlalchemy.sql import extract



def add_user(name, username, password, diachi, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(), username=username, password=password, diachi=diachi,
                email=kwargs.get('email'), avatar=kwargs.get('avatar'))

    db.session.add(user)
    db.session.commit()


def check_login(username, password, role=UserRole.USER):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username),
                                 User.password.__eq__(password),
                                 User.user_role.__eq__(role)).first()


def check_admin_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username),
                                 User.password.__eq__(password),
                                 User.user_role != UserRole.USER).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)



