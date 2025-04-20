# app/services/query_flight_passenger_service.py

from app.models.checkin import Checkin
from app.models.flight import Flight
from datetime import datetime
from app import db

class QueryFlightPassengerService:
    @staticmethod
    def get_passenger_list(query_dto):
        try:
            # Find the flight by flight_number
            flight = Flight.query.filter_by(flight_number=query_dto.flight_number).first()
            if not flight:
                return {"transaction_status": "failed", "message": "Flight not found"}

            # Validate the flight date
            flight_date = datetime.strptime(query_dto.date, "%Y-%m-%d").date()
            if flight.date_from != flight_date:
                return {"transaction_status": "failed", "message": "Flight date mismatch"}

            # Query for passengers who checked in on the given date and flight
            passengers_query = Checkin.query.filter_by(flight_number=query_dto.flight_number, date=flight_date)

            # Pagination
            passengers = passengers_query.offset((query_dto.page - 1) * query_dto.limit).limit(query_dto.limit).all()

            # Format the passenger data
            passenger_list = [{
                "passenger_name": passenger.passenger_name,
                "seat_number": passenger.seat_number,
                "flight_date": passenger.date.isoformat()
            } for passenger in passengers]

            return {
                "transaction_status": "success",
                "passengers": passenger_list
            }

        except Exception as e:
            return {"transaction_status": "failed", "message": str(e)}
