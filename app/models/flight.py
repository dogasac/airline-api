from app import db
from datetime import datetime

class Flight(db.Model):
    __tablename__ = 'flights'

    flight_number = db.Column(db.Integer, primary_key=True)
    airport_from = db.Column(db.String(50))
    airport_to = db.Column(db.String(50))
    date_from = db.Column(db.Date)  # sadece tarih
    date_to = db.Column(db.Date)    # sadece tarih
    duration = db.Column(db.Integer)
    capacity = db.Column(db.Integer)

    def __repr__(self):
        return f"<Flight {self.flight_number}>"
