# /app/services/flight_services.py
from app.models.flight import Flight
from app import db
from datetime import datetime
from app.dto.flight_dto import FlightDTO

def add_flight(data):
    """
    Add a new flight to the airline schedule
    """
    try:
        # Parse the dates as date-only (without time)
        date_from = datetime.strptime(data['date_from'], "%Y-%m-%d").date()
        date_to = datetime.strptime(data['date_to'], "%Y-%m-%d").date()

        new_flight = Flight(
            airport_from=data['airport_from'],
            airport_to=data['airport_to'],
            date_from=date_from,
            date_to=date_to,
            duration=data['duration'],
            capacity=data['capacity']
        )

        db.session.add(new_flight)
        db.session.commit()

        # FlightDTO döndür
        flight_dto = FlightDTO(
            new_flight.flight_number, 
            new_flight.airport_from, 
            new_flight.airport_to, 
            new_flight.date_from, 
            new_flight.date_to, 
            new_flight.duration
        )

        return {"transaction_status": "success", "flight_number": flight_dto.flight_number}

    except Exception as e:
        return {"transaction_status": "failed", "message": str(e)}

def query_flights(date_from_str, date_to_str, airport_from, airport_to, number_of_people, trip_type):
    """
    Query available flights based on date range, airports, number of people, and trip type
    """
    try:
        # Parse the dates as date-only (without time)
        date_from = datetime.strptime(date_from_str, "%Y-%m-%d").date()
        date_to = datetime.strptime(date_to_str, "%Y-%m-%d").date()

        flights_query = Flight.query.filter(
            Flight.airport_from == airport_from,
            Flight.airport_to == airport_to,
            Flight.date_from >= date_from,
            Flight.date_to <= date_to,
            Flight.capacity >= number_of_people
        )

        if trip_type == 'round-trip':
            flights_query = flights_query.filter(Flight.date_to >= date_from)

        flights = flights_query.all()

        # DTO'yu uçuşlar için oluştur
        flight_list = [
            FlightDTO(flight.flight_number, flight.airport_from, flight.airport_to, flight.date_from, flight.date_to, flight.duration).to_dict()
            for flight in flights if flight.capacity > 0
        ]

        return {"flights": flight_list}

    except Exception as e:
        return {"transaction_status": "failed", "message": str(e)}
