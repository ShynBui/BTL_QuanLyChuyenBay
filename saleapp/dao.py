from flask_login import current_user

from saleapp import app, db, encoding, decoding
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
    if not al:
        return []
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
    return PriceOfFlight.query.filter(
        and_(PriceOfFlight.flight_id.__eq__(flight_id), PriceOfFlight.rank_id.__eq__(rank_id))).first()



def save_order(cart, total_price):
    ord = PurchaseOrder(total=total_price, user=current_user)
    db.session.add(ord)
    for c in cart['seats']:
        cus = get_customer(cart['seats'][c]['customer']['serial'])
        if cus:
            t = PlaneTicket(subTotal=cart['seats'][c]['price'], seat_id=c, customer_id=cus.id, order=ord,
                            flight_id=cart['flight_id'])
            db.session.add(t)
        else:
            new_cus = Customer(serial=encoding.encoding_no1(cart['seats'][c]['customer']['serial']),
                               name=encoding.encoding_no1(cart['seats'][c]['customer']['name']),
                               gender=cart['seats'][c]['customer']['gender'], dob=cart['seats'][c]['customer']['dob'],
                               email=encoding.encoding_no1(cart['seats'][c]['customer']['email']),
                               phone=encoding.encoding_no1(cart['seats'][c]['customer']['phone']))
            db.session.add(new_cus)
            t = PlaneTicket(subTotal=cart['seats'][c]['price'], seat_id=c, customer=new_cus, order=ord,
                            flight_id=cart['flight_id'])
            db.session.add(t)
    db.session.commit()


def get_customer(serial):
    encodeSerial = encoding.encoding_no1(serial)
    cus = Customer.query.filter(Customer.serial.__eq__(encodeSerial)).first()
    return cus


def get_order(user_id, order_id=None):
    ords = PurchaseOrder.query.filter(PurchaseOrder.user_id.__eq__(user_id)) \
        .order_by(PurchaseOrder.orderDate.desc())
    if order_id:
        ords = ords.filter(PurchaseOrder.id.__eq__(order_id))
        return ords.first()
    return ords.all()


def get_newest_order(user_id):
    ords = PurchaseOrder.query.filter(PurchaseOrder.user_id.__eq__(user_id)) \
        .order_by(PurchaseOrder.orderDate.desc())
    return ords.first()
# def get_order(user_id)
# if __name__ == '__main__':
#     with app.app_context():
