from app import db
from app.models.ticket import Ticket
from app.models.flight import Flight
import random
import string
from datetime import datetime

class TicketService:

    @staticmethod
    def buy_ticket(flight_number, flight_date_str, passenger_names):
        try:
            # Convert the string date to a datetime object
            flight_date = datetime.strptime(flight_date_str, '%Y-%m-%d').date()

            # Query the flight
            flight = Flight.query.filter_by(flight_number=flight_number).first()

            if not flight:
                return {'error': 'Flight not found'}, 404

            # Check if there are enough available seats
            if flight.capacity < len(passenger_names):
                return {'error': 'Sold out'}, 404

            # Create tickets for each passenger
            ticket_numbers = []
            for passenger in passenger_names:
                # Generate a random ticket number
                ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                ticket_numbers.append(ticket_number)

                # Create a ticket entry
                ticket = Ticket(
                    flight_number=flight_number,
                    date=flight_date,  # Store the date as a date object
                    passenger_name=passenger,
                    ticket_number=ticket_number
                )
                db.session.add(ticket)

            # Decrease the available capacity
            flight.capacity -= len(passenger_names)

            # Commit changes to the database
            db.session.commit()

            return {
                'transaction_status': 'success',
                'ticket_numbers': ticket_numbers,
                'remaining_capacity': flight.capacity
            }, 200

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500
