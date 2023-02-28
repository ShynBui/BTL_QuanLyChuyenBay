
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




