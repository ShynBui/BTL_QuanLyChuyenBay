from sqlalchemy import DECIMAL, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, backref
from saleapp import db, app
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
    STAFF = 3
    IMPORTER = 4


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default='https://image.thanhnien.vn/1200x630/Uploaded/2022/xdrkxrvekx/2015_11_18/anonymous-image_fgnd.jpg')
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    diachi = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    message = relationship('Message', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Customer(BaseModel):
    serial = Column(String(25), nullable=False)
    name = Column(String(50), nullable=False)
    gender = Column(String(10), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    tickets = relationship('PlaneTicket', backref='customer', lazy=True)

    def __str__(self):
        return self.name


class Airplane(BaseModel):
    name = Column(String(50), nullable=False, unique=True)
    image = Column(String(100))
    flights = relationship('Flight', backref='airplane', lazy=True)

    def __str__(self):
        return self.name


class Airport(BaseModel):
    name = Column(String(50), nullable=False)
    image = Column(String(100))
    code = Column(String(10), nullable=False, unique=True)
    location = Column(String(100), nullable=False)
    FAMediums = relationship('Flight_AirportMedium', backref='airport', lazy=True)
    departing_airline = relationship("Airline", primaryjoin="Airline.departing_airport_id==Airport.id",
                                     backref="departing_airport", lazy=True)
    arriving_airline = relationship("Airline", primaryjoin="Airline.arriving_airport_id==Airport.id",
                                    backref="arriving_airport", lazy=True)

    def __str__(self):
        return self.name


class Rank(BaseModel):
    name = Column(String(25), nullable=False)
    seats = relationship('Seat', backref='rank', lazy=True)
    prices = relationship('PriceOfFlight', backref='rank', lazy=True)

    def __str__(self):
        return self.name


class Seat(BaseModel):
    name = Column(String(3), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    rank_id = Column(Integer, ForeignKey(Rank.id), nullable=False)
    tickets = relationship('PlaneTicket', backref='seat', lazy=True)

    def __str__(self):
        return self.name


class PurchaseOrder(BaseModel):
    total = Column(Float, nullable=False)
    orderDate = Column(DateTime, default=datetime.now())
    tickets = relationship('PlaneTicket', backref='order', lazy=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __str__(self):
        return self.id


class Airline(BaseModel):
    departing_airport_id = Column(Integer, ForeignKey(Airport.id), nullable=False)
    arriving_airport_id = Column(Integer, ForeignKey(Airport.id), nullable=False)
    flights = relationship('Flight', backref='airline', lazy=True)

    def __str__(self):
        return f'{self.departing_airport.name} {self.arriving_airport.name}'


class Flight(BaseModel):
    departing_at = Column(DateTime, nullable=False)
    arriving_at = Column(DateTime, nullable=False)
    airplane_id = Column(Integer, ForeignKey(Airplane.id), nullable=False)
    airline_id = Column(Integer, ForeignKey(Airline.id), nullable=False)
    airportMediums = relationship('Flight_AirportMedium', backref='flight', lazy=True)
    tickets = relationship('PlaneTicket', backref='flight', lazy=True)
    prices = relationship('PriceOfFlight', backref='flight', lazy=True)

    def __str__(self):
        return f'từ {self.airline.departing_airport.name} đến {self.airline.arriving_airport.name}'


class PriceOfFlight(BaseModel):
    rank_id = Column(Integer, ForeignKey(Rank.id), nullable=False)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return self.price


class Flight_AirportMedium(BaseModel):
    stop_time_begin = Column(DateTime, nullable=False)
    stop_time_finish = Column(DateTime, nullable=False)
    description = Column(Text)
    airport_id = Column(Integer, ForeignKey(Airport.id), nullable=False)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)

    def __str__(self):
        return self.airport.name


class PlaneTicket(BaseModel):
    subTotal = Column(Float, nullable=False)
    seat_id = Column(Integer, ForeignKey(Seat.id), nullable=False)
    customer_id = Column(Integer, ForeignKey(Customer.id), nullable=False)
    order_id = Column(Integer, ForeignKey(PurchaseOrder.id), nullable=False)
    flight_id = Column(Integer, ForeignKey(Flight.id), nullable=False)

    def __str__(self):
        return self.id


class Room(db.Model):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    is_reply = Column(Boolean, default=True)
    date = Column(DateTime, default=datetime.now())
    message = relationship('Message', backref='room', lazy=True)

    def __str__(self):
        return self.name

class Message(db.Model):
    __tablename__ = 'message'

    id = id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.id), nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False, primary_key=True)

    content = Column(String(255), default= '')
    date = Column(DateTime, default= datetime.now())

    def __str__(self):
        return self.content


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        a1 = Airplane(name="A001")
        a2 = Airplane(name="A002")
        a3 = Airplane(name="A003")
        a4 = Airplane(name="A004")
        a5 = Airplane(name="A005")
        db.session.add_all([a1, a2, a3, a4, a5])

        ap1 = Airport(name="Sân bay QT Nội Bài", code="HAN", location="Hà Nội")
        ap2 = Airport(name="Sân bay QT Tân Sơn Nhất", code="SGN", location="Hồ Chí Minh")
        ap3 = Airport(name="Sân bay QT Đà Nẵng", code="DAD", location="Đà Nẵng")
        ap4 = Airport(name="Sân bay QT Phú Quốc", code="PQC", location="Kiên Giang")
        ap = [ap1, ap2, ap3, ap4]
        db.session.add_all(ap)

        r1 = Rank(name="Thương gia")
        r2 = Rank(name="Phổ thông")
        db.session.add_all([r1, r2])

        # Khởi tạo ghế thương gia
        for i in range(4):
            for j in range(4):
                col = chr(65 + j)
                name = str(col) + "0" + str(i+1)
                s = Seat(name=name, rank_id=1)
                db.session.add(s)

        # Khởi tạo ghế phổ thông
        for i in range(4, 14):
            for j in range(4):
                col = chr(65 + j)
                if i < 9:
                    row = "0" + str(i+1)
                else:
                    row = str(i+1)
                name = str(col) + row
                s = Seat(name=name, rank_id=2)
                db.session.add(s)


        # Khởi tạo airline
        for i in range(len(ap)):
            for j in range(len(ap)):
                if i != j:
                    al = Airline(departing_airport_id=i + 1, arriving_airport_id=j + 1)
                    db.session.add(al)

        # Khởi tạo flight
        f1 = Flight(departing_at="2023-03-03 05:00", arriving_at="2023-03-03 07:15", airplane_id=1, airline_id=4)
        p11 = PriceOfFlight(rank_id=1, flight=f1, price="6000")
        p12 = PriceOfFlight(rank_id=2, flight=f1, price="1900")
        db.session.add_all([f1, p11, p12])

        f2 = Flight(departing_at="2023-03-03 07:00", arriving_at="2023-03-03 09:15", airplane_id=2, airline_id=4)
        p21 = PriceOfFlight(rank_id=1, flight=f2, price="6000")
        p22 = PriceOfFlight(rank_id=2, flight=f2, price="2300")
        db.session.add_all([f2, p21, p22])

        f3 = Flight(departing_at="2023-03-03 11:45", arriving_at="2023-03-03 19:40", airplane_id=3, airline_id=4)
        p31 = PriceOfFlight(rank_id=1, flight=f3, price="9000")
        p32 = PriceOfFlight(rank_id=2, flight=f3, price="2600")
        fa31 = Flight_AirportMedium(stop_time_begin="2023-03-03 13:35", stop_time_finish="2023-03-03 18:45",
                                    airport_id=3, flight=f3)
        db.session.add_all([f3, p31, p32, fa31])

        db.session.commit()