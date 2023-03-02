
from flask_login import current_user

from saleapp import app, db
from sqlalchemy import or_, and_, not_, func, extract
from sqlalchemy.orm import aliased
from saleapp.models import *


def get_flights(FROM, TO, date):
    departing_airport = aliased(Airport)
    arriving_airport = aliased(Airport)
    al = db.session.query(Airline.id) \
        .join(departing_airport, Airline.departing_airport_id.__eq__(departing_airport.id)) \
        .join(arriving_airport, Airline.arriving_airport_id.__eq__(arriving_airport.id)) \
        .filter(and_(departing_airport.code.__eq__(FROM), arriving_airport.code.__eq__(TO))).first()

    f = Flight.query
    f = f.filter(and_(Flight.airline_id.__eq__(al.id), func.date(Flight.departing_at).__eq__(date)))
    return f.all()


def get_airport():
    return Airport.query.all()


def get_rank(rank_id=None):
    r = Rank.query
    if rank_id:
        r = r.filter(Rank.id.__eq__(rank_id))
        return r.first()
    return r.all()


def get_flight(id):
    return Flight.query.filter(Flight.id.__eq__(id)).first()


def get_seat(rank_id=None):
    s = Seat.query
    if rank_id:
        s = s.filter(Seat.rank_id.__eq__(rank_id))
    return s.all()


def is_seat_available(seat_id, flight_id):
    tickets_of_flight = PlaneTicket.query.filter(and_(PlaneTicket.flight_id.__eq__(flight_id),
                                                      PlaneTicket.seat_id.__eq__(seat_id)))
    t = tickets_of_flight.first()
    if t is None:
        return True
    else:
        return False


def get_price(flight_id, rank_id):
    return PriceOfFlight.query.filter(and_(PriceOfFlight.flight_id.__eq__(flight_id), PriceOfFlight.rank_id.__eq__(rank_id))).first()


# if __name__ == '__main__':
#     with app.app_context():