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
    avatar = Column(Text, default='https://image.thanhnien.vn/1200x630/Uploaded/2022/xdrkxrvekx/2015_11_18/anonymous-image_fgnd.jpg')
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    diachi = Column(String(100), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    message = relationship('Message', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Profile(db.Model):
    __tablename__ = 'profiles'

    serial = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String(12), nullable=False)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    dob = Column(DateTime, nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False)
    isSupervisor = Column(Boolean, default=False)

    def __str__(self):
        return str(self.id)


class AirPlane(db.Model):
    __tablename__ = 'airplanes'

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    total_seat = Column(Integer, nullable=False)
    image = Column(String(100))

    def __str__(self):
        return str(self.id)


class AirPort(db.Model):
    __tablename__ = 'airports'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    image = Column(String(100))
    location = Column(String(100), nullable=False)

    def __str__(self):
        return str(self.name)


class AirLine(db.Model):
    __tablename__ = 'airlines'

    id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)

    from_airport_id = Column(Integer, ForeignKey(AirPort.id, ondelete="CASCADE", onupdate="cascade"), nullable=False)
    to_airport_id = Column(Integer, ForeignKey(AirPort.id, ondelete="CASCADE"), nullable=False)

    from_airport = relationship("AirPort", foreign_keys=[from_airport_id], lazy=True,
                                passive_deletes=True, cascade="all, delete")
    to_airport = relationship("AirPort", foreign_keys=[to_airport_id], lazy=True,
                              passive_deletes=True, cascade="all, delete")

    def __str__(self):
        return str(self.name)


flight_regulation = db.Table('flight_regulation',
    Column('flight_id', String(10), ForeignKey('flights.id', ondelete="CASCADE", onupdate="cascade"), primary_key=True),
    Column('regulation_id', Integer, ForeignKey('regulations.id', ondelete="CASCADE", onupdate="cascade"), primary_key=True)
)


class Flight(db.Model):
    __tablename__ = 'flights'

    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=False)
    departing_at = Column(DateTime, nullable=False)
    arriving_at = Column(DateTime, nullable=False)

    plane_id = (Column(String(10), ForeignKey(AirPlane.id, ondelete="CASCADE", onupdate="cascade"), nullable=False))
    airline_id = (Column(String(10), ForeignKey(AirLine.id, ondelete="CASCADE", onupdate="cascade"), nullable=False))
    planes = relationship("AirPlane", foreign_keys=[plane_id], lazy=True,
                          passive_deletes=True, cascade="all, delete")
    airlines = relationship("AirLine", foreign_keys=[airline_id], lazy=True,
                            passive_deletes=True, cascade="all, delete")

    regulations = relationship("Regulation", secondary=flight_regulation, lazy='subquery',
                            backref=backref('regulations', lazy=True), passive_deletes=True, cascade="all, delete")

    def __str__(self):
        return str(self.name)


class Seat(db.Model):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    status = Column(Boolean, default=False)

    flight_id = Column(String(10), ForeignKey(Flight.id, ondelete="CASCADE", onupdate="cascade"), nullable=False)
    flights = relationship("Flight", foreign_keys=[flight_id], lazy=True,
                           passive_deletes=True, cascade="all, delete")

    def __str__(self):
        return str(self.id)


class FA_Regulation(db.Model):
    flight_id = Column(String(10), ForeignKey('flight_airport_mediums.flight_id', ondelete="CASCADE",
                            onupdate="cascade"), primary_key=True)
    airport_id = Column(Integer, ForeignKey('flight_airport_mediums.airport_medium_id', ondelete="CASCADE",
                            onupdate="cascade"), primary_key=True)
    regulation_id = Column(Integer, ForeignKey('regulations.id', ondelete="CASCADE",
                                                onupdate="cascade"), primary_key=True)

    flights = relationship("Flight_AirportMedium", foreign_keys=[flight_id], lazy='subquery',
                           passive_deletes=True, cascade="all, delete")
    airports = relationship("Flight_AirportMedium", foreign_keys=[airport_id], lazy='subquery',
                           passive_deletes=True, cascade="all, delete")
    regs = relationship("Regulation", foreign_keys=[regulation_id], lazy='subquery',
                        passive_deletes=True, cascade="all, delete")


class Flight_AirportMedium(db.Model):
    __tablename__ = 'flight_airport_mediums'

    name = Column(String(50), nullable=False)
    stop_time_begin = Column(DateTime, nullable=False)
    stop_time_finish = Column(DateTime, nullable=False)
    description = Column(Text)

    flight_id = Column(String(10), ForeignKey(Flight.id, ondelete="CASCADE", onupdate="cascade"), primary_key=True)
    airport_medium_id = Column(Integer, ForeignKey(AirPort.id, ondelete="CASCADE", onupdate="cascade"), primary_key=True)
    flights = relationship("Flight", foreign_keys=[flight_id], lazy=True,
                           passive_deletes=True, cascade="all, delete")
    airports = relationship("AirPort", foreign_keys=[airport_medium_id], lazy=True,
                            passive_deletes=True, cascade="all, delete")

    def __str__(self):
        return str(self.name)


ticket_regulation = db.Table('ticket_regulation',
    Column('ticket_id', Integer, ForeignKey('tickets.id', ondelete="CASCADE", onupdate="cascade"), primary_key=True),
    Column('regulation_id', Integer, ForeignKey('regulations.id', ondelete="CASCADE", onupdate="cascade"), primary_key=True)
)


class PlaneTicket(db.Model):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer, nullable=False)
    price = Column(DECIMAL(18, 2), nullable=False)
    date = Column(DateTime, default=datetime.now())

    place = Column(Integer, ForeignKey(AirPort.id, ondelete="CASCADE", onupdate="cascade"))
    profile_id = (Column(Integer, ForeignKey(Profile.serial, ondelete="CASCADE", onupdate="cascade"), nullable=False))
    flight_id = (Column(String(10), ForeignKey(Flight.id, ondelete="CASCADE", onupdate="cascade"), nullable=False))
    seat_id = (Column(Integer, ForeignKey(Seat.id, ondelete="CASCADE", onupdate="cascade"), nullable=False))
    user_id = (Column(Integer, ForeignKey(User.id, ondelete="CASCADE", onupdate="cascade")))

    places = relationship("AirPort", foreign_keys=[place], lazy=True,
                          cascade="all, delete", passive_deletes=True)
    profiles = relationship("Profile", foreign_keys=[profile_id], lazy=True,
                            cascade="all, delete", passive_deletes=True)
    flights = relationship("Flight", foreign_keys=[flight_id], lazy=True,
                           cascade="all, delete", passive_deletes=True)
    seats = relationship("Seat", foreign_keys=[seat_id], lazy=True, uselist=False,
                         cascade="all, delete", passive_deletes=True)
    users = relationship("User", foreign_keys=[user_id], lazy=True,
                         cascade="all, delete", passive_deletes=True)

    def __str__(self):
        return str(self.id)


class Regulation(db.Model):
    __tablename__ = 'regulations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    value = Column(String(50), nullable=False)
    description = Column(Text)

    tickets = relationship("PlaneTicket", secondary=ticket_regulation, lazy='subquery',
                        backref=backref('tickets', lazy=True), passive_deletes=True, cascade="all, delete")

    def __str__(self):
        return str(self.id)

    def get_value(self):
        return self.value

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
        #
        # db.drop_all()
        db.create_all()


        db.session.commit()