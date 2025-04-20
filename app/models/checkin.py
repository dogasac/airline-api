from datetime import date
from app import db

class Checkin(db.Model):
    __tablename__ = 'checkins'

    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.Integer, nullable=False)
    passenger_name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)  # Sadece tarih (date) olarak değiştirdik
    seat_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Checkin {self.passenger_name} for flight {self.flight_number}>"
