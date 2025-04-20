from app.models.ticket import Ticket
from app.models.checkin import Checkin
from app import db

class CheckinService:
    @staticmethod
    def checkin_passenger(dto):
        # 1. Yolcunun bu uçuş için bileti var mı?
        ticket = Ticket.query.filter_by(
            flight_number=dto.flight_number,
            date=dto.date,
            passenger_name=dto.passenger_name
        ).first()

        if not ticket:
            return {
                "transaction_status": "failed",
                "message": "Passenger does not have a valid ticket for this flight"
            }

        # 2. Daha önce check-in yapılmış mı?
        existing_checkin = Checkin.query.filter_by(
            flight_number=dto.flight_number,
            date=dto.date,
            passenger_name=dto.passenger_name
        ).first()

        if existing_checkin:
            return {
                "transaction_status": "failed",
                "message": "Passenger already checked in"
            }

        # 3. Koltuk numarası ata (örneğin en son numaradan sonra gelen)
        last_seat = db.session.query(db.func.max(Checkin.seat_number)).filter_by(
            flight_number=dto.flight_number,
            date=dto.date
        ).scalar()

        new_seat_number = 1 if last_seat is None else last_seat + 1

        # 4. Check-in kaydını oluştur
        checkin = Checkin(
            flight_number=dto.flight_number,
            date=dto.date,
            passenger_name=dto.passenger_name,
            seat_number=new_seat_number
        )
        db.session.add(checkin)
        db.session.commit()

        return {
            "transaction_status": "success",
            "message": "Checkin successful",
            "seat_number": new_seat_number
        }
