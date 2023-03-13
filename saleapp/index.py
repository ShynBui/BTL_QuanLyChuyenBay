import math
from datetime import datetime
from flask import render_template, request, redirect, session, jsonify, url_for
from saleapp import app, admin, login, untils, socketio, dao, utils, sendmail
from saleapp.models import UserRole
from flask_login import login_user, logout_user, login_required, current_user
import cloudinary.uploader
from flask_socketio import SocketIO, emit, join_room


@app.route("/", methods=('GET', 'POST'))
def home():
    flights = untils.load_flights()
    data_fill = flights
    len_of_flights = len(data_fill)
    if request.method == "POST":
        data_fill = []
        start = request.form['start']
        finish = request.form['finish']
        date = request.form['date']
        date = datetime.strptime(date, "%Y-%m-%d").date()
        for f in flights:
            f_d = f.departing_at.date()
            if f.airline.departing_airport.name == start and f.airline.arriving_airport.name == finish \
                    and f_d == date:
                if 'vip' in request.form:
                    p = untils.get_prices_of_flight(f.id)
                    for pr in p:
                        if pr.rank.name == 'Thương gia':
                            data_fill.append(f)
                else:
                    data_fill.append(f)
        len_of_flights = len(data_fill)
    return render_template('index.html', data_fill=data_fill, len_of_flights=len_of_flights)

@app.route("/news")
def news():
    return render_template('news.html')


# socket

@app.route("/chatroom")
def chat_room():
    if current_user.is_authenticated:
        pass
    else:
        return redirect(url_for('user_signin'))


    user_name = current_user.name
    room = untils.get_chatroom_by_user_id(id=current_user.id)

    print(room.room_id)

    user_send = [untils.get_user_by_id(x.user_id).name for x in untils.load_message(room.room_id)]

    user_image = [untils.get_user_by_id(x.user_id).avatar for x in untils.load_message(room.room_id)]

    user_id = [x.user_id for x in untils.load_message(room.room_id)]

    host_avatar = untils.get_host_room_avatar(room.room_id);

    user_send.pop(0)
    user_image.pop(0)
    user_id.pop(0)

    print(user_send)

    if user_name and room:

        print(untils.load_message(room.room_id)[0].content)
        return render_template('chatroom.html', user_name=user_name, room=room.room_id, name=current_user.name,
                               message=untils.load_message(room.room_id), room_id=int(room.room_id),
                               user_send=user_send, n=len(user_send), user_image=user_image, user_id=user_id,
                               room_name=untils.get_chatroom_by_id(room.room_id),
                               host_avatar=host_avatar);
    else:
        return redirect(url_for('home'))


@app.route("/admin/chatadmin/<int:room_id>")
def chat_room_admin(room_id):
    if current_user.user_role == UserRole.ADMIN:
        print(room_id)
        user_name = current_user.name
        room = untils.get_chatroom_by_room_id(id=room_id)

        user_send = [untils.get_user_by_id(x.user_id).name for x in untils.load_message(room.room_id)]

        user_image = [untils.get_user_by_id(x.user_id).avatar for x in untils.load_message(room.room_id)]

        user_id = [x.user_id for x in untils.load_message(room.room_id)]

        user_send.pop(0)
        user_image.pop(0)
        user_id.pop(0)

        host_avatar = untils.get_host_room_avatar(room.room_id);

        if user_name and room:
            return render_template('chatroom.html', user_name=user_name, room=room.room_id, name=current_user.name,
                                   message=untils.load_message(room.room_id), room_id=int(room.room_id),
                                   user_send=user_send, n=len(user_send), user_image=user_image, user_id=user_id,
                                   room_name=untils.get_chatroom_by_id(room.room_id),
                                   host_avatar=host_avatar);

    return redirect(url_for('home'));


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))

    app.logger.info("{}".format(data['user_avatar']))
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('save_message')
def handle_save_message_event(data):
    # app.logger.info("2.all_mess: " + str(data['all_message']))
    app.logger.info("2.room_id: " + str(data['room']))

    untils.save_chat_message(room_id=int(data['room']), message=data['message'], user_id=current_user.id)

    if (current_user.user_role == UserRole.ADMIN):
        print("Dd")
        untils.change_room_status(data['room'], 1)

    if (current_user.user_role == UserRole.USER):
        print("Dd1")
        untils.change_room_status(data['room'], 0)


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


@app.route('/admin-login', methods=["POST", "GET"])
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
        seats = dao.get_seat()
        vip_seats_count = 0
        seats_count = 0
        for s in seats:
            if dao.is_seat_available(seat_id=s.id, flight_id=f.id):
                if s.rank_id == 1:
                    vip_seats_count += 1
                else:
                    seats_count += 1
        f.fa_amount = len(f.airportMediums)
        f.vip_seats_count = vip_seats_count
        f.seats_count = seats_count
        if vip_seats_count == 0 and seats_count == 0:
            flights.remove(f)
    return render_template('buyticket2.html', flights=flights)


@app.route('/api/cart/select-flight-<flight_id>')
def select_flight(flight_id):
    key = app.config['CART_KEY']
    if key not in session:
        session[key] = {}
    cart = session.get(key)
    cart["flight_id"] = flight_id
    session[key] = cart
    return jsonify(cart)


@app.route('/api/cart/select-seat-<seat_id>', methods=['POST'])
def select_seat(seat_id):
    key = app.config['CART_KEY']
    if key not in session or "flight_id" not in session[key]:
        return jsonify({"status": 404})

    cart = session[key]
    data = request.json
    if "seats" not in session[key]:
        cart["seats"] = {}
    price = dao.get_price(flight_id=cart["flight_id"], rank_id=str(data['rank_id']))
    if seat_id not in cart["seats"]:
        cart["seats"][seat_id] = {
            "id": str(data['id']),
            "name": str(data['name']),
            "rank_id": data['rank_id'],
            "rank": str(dao.get_rank(data['rank_id'])),
            "price": price.price
        }
        session[key] = cart
        return jsonify({"status": 201, "cart": session[key]})
    else:
        del cart["seats"][seat_id]
        session[key] = cart
        return jsonify({"status": 200, "cart": session[key], "seat_id": seat_id})


@app.route('/api/cart/total')
def total():
    key = app.config['CART_KEY']
    cart = session.get(key)
    return jsonify(utils.cart_stats(cart["seats"]))


@app.route('/buy-ticket/step-3/')
def buy_ticket3():
    key = app.config['CART_KEY']
    if key not in session or "flight_id" not in session[key]:
        return redirect("/buy-ticket")
    cart = session.get(key)
    if "seats" in cart:
        del cart["seats"]
    session[key] = cart
    flight_id = cart["flight_id"]
    vip_seats = dao.get_seat(rank_id=1)
    seats = dao.get_seat(rank_id=2)
    for vs in vip_seats:
        vs.available = dao.is_seat_available(seat_id=vs.id, flight_id=flight_id)
    for s in seats:
        s.available = dao.is_seat_available(seat_id=s.id, flight_id=flight_id)

    vs_mtrx = []
    i = 0
    while True:
        char = str(chr(65 + i))
        col = [vs for vs in vip_seats if vs.name.startswith(char)]
        if not col:
            break
        vs_mtrx.append(col)
        i = i + 1

    i = 0
    s_mtrx = []
    while True:
        char = str(chr(65 + i))
        col = [s for s in seats if s.name.startswith(char)]
        if not col:
            break
        s_mtrx.append(col)
        i = i + 1
    return render_template('selectseat.html', vip_seats=vs_mtrx, seats=s_mtrx, vs_count=len(vs_mtrx[0]),
                           s_count=len(s_mtrx[0]))


@app.route("/buy-ticket/step-4")
def cus_form():
    key = app.config['CART_KEY']
    if key not in session or "flight_id" not in session[key] or "seats" not in session[key] or len(
            session[key]["seats"]) == 0:
        return redirect("/buy-ticket")
    key = app.config['CART_KEY']
    seats = session[key]["seats"]
    return render_template('fillform.html', seats=seats)


@app.route("/api/index/")
def airports():
    data = []

    for a in untils.load_airports():
        data.append({
            'id': a.id,
            'name': a.name
        })

    return jsonify(data)


@app.route("/api/index/price/")
def prices():
    data = []

    for f in untils.load_flights():
        p = untils.get_prices_of_flight(f.id)
        for pr in p:
            data.append({
                'flight_id': pr.flight_id,
                'rank': pr.rank.name,
                'price': pr.price
            })

    return jsonify(data)


@app.route("/api/cart/pay", methods=['POST'])
def pay():
    data = request.json
    key = app.config['CART_KEY']
    cart = session.get(key)
    for s in cart["seats"]:
        cart["seats"][s]['customer'] = data['data'][s]
    total_price = utils.cart_stats(cart["seats"])['total_price']
    dao.save_order(cart=cart, total_price=total_price)
    o = dao.get_newest_order(user_id=current_user.id)

    del session[key]
    return jsonify({"order_id": o.id})


@app.route("/orders")
def get_orders():
    id = current_user.id
    ords = dao.get_order(user_id=id)
    for o in ords:
        for t in o.tickets:
            o.flight = t.flight
            break

    return render_template('orders.html', orders=ords)


@app.route('/order/<order_id>')
def detail_order(order_id):
    id = current_user.id

    ords = dao.get_order(user_id=id, order_id=order_id)
    return render_template('tickets.html', tickets=ords.tickets)


@app.route('/api/otp', methods=["POST"])
def send_otp():
    data = request.json
    email = data["email"]
    name = data["name"]
    otp = utils.generateOTP()
    sendmail.send(name, email, otp)

    return jsonify({"otp": otp})


if __name__ == '__main__':
    socketio.run(app, debug=True)
