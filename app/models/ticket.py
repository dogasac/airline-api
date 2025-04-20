from app import db
import random
import string

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.Integer, db.ForeignKey('flights.flight_number'), nullable=False)
    date = db.Column(db.Date, nullable=False)  # Sadece tarih olarak değiştirildi
    passenger_name = db.Column(db.String(100), nullable=False)
    ticket_number = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"<Ticket {self.ticket_number}>"

    @staticmethod
    def generate_ticket_number():
        """Generate a random ticket number"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
