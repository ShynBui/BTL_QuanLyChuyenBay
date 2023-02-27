import math
import datetime
from flask import render_template, request, redirect, session, jsonify, url_for
from saleapp import app, admin, login, untils, socketio, dao
from saleapp.models import UserRole
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader
from flask_socketio import SocketIO, emit, join_room

@app.route("/")
def home():
    return render_template('index.html')

#socket

@app.route("/chatroom")
def chat_room():
    user_name = current_user.username
    room = 123

    if user_name and room:
        return render_template('chatroom.html', user_name=user_name, room=room)
    else:
        return redirect(url_for('home'))


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])

@socketio.on('join_room')
def handle_send_room_event(data):
    app.logger.info(data['username'] + " has sent message to the room " + data['room'] + ": ")
    join_room(data['room'])

    socketio.emit('join_room_announcement', data, room=data['room'])


@app.route('/register', methods=['get', 'post'])
def user_register():
    err_msg = ""
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        diachi = request.form.get('diachi')
        confirm = request.form.get('confirm')
        avatar_path = None

    try:
        if str(password) == str(confirm):
            avatar = request.files.get('avatar')
            if avatar:
                res = cloudinary.uploader.upload(avatar)
                avatar_path = res['secure_url']

            untils.add_user(name=name,
                            username=username,
                            password=password,
                            diachi=diachi,
                            email=email,
                            avatar=avatar_path)
            return redirect(url_for('user_signin'))
        else:
            err_msg = "Mat khau khong khop"
            # print(err_msg)
    except Exception as ex:
        pass
        # err_msg = 'He thong ban' + str(ex)
        # print(err_msg)

    return render_template('register.html', err_msg=err_msg)


@app.route('/user-login', methods=['get', 'post'])
def user_signin():
    err_msg = ""

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = untils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            next = request.args.get('next', 'home')
            return redirect(url_for(next))
        else:
            err_msg = "Sai tên đăng nhập hoặc mật khẩu"

    return render_template('login.html', err_msg=err_msg)


@app.route('/admin-login', methods=['post'])
def signin_admin():
    username = request.form.get('username')
    password = request.form.get('password')

    # user = untils.check_login(username=username, password=password, role=UserRole.ADMIN)
    user = untils.check_admin_login(username=username, password=password)
    if user:
        print(1)
        login_user(user=user)

    return redirect('/admin')


@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('home'))


@login.user_loader
def user_load(user_id):
    return untils.get_user_by_id(user_id=user_id)


@app.route('/buy-ticket')
def buy_ticket():
    airports = dao.get_airport()
    return render_template('buyticket.html', airports=airports)


@app.route('/buy-ticket/step-2')
def buy_ticket2():
    FROM = request.args.get('from')
    TO = request.args.get('to')
    date = request.args.get('date')
    flights = dao.get_flights(FROM, TO, date)
    for f in flights:
        f.fa_amount = len(f.airportMediums)
    return render_template('buyticket2.html', flights=flights)


@app.route('/buy-ticket/select-seat')
def select_seat():
    return render_template('selectseat.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
