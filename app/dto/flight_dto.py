

class FlightDTO:
    def __init__(self, flight_number, airport_from, airport_to, date_from, date_to, duration):
        self.flight_number = flight_number
        self.airport_from = airport_from
        self.airport_to = airport_to
        self.date_from = date_from
        self.date_to = date_to
        self.duration = duration

    def to_dict(self):
        return {
            'flight_number': self.flight_number,
            'airport_from': self.airport_from,
            'airport_to': self.airport_to,
            'date_from': self.date_from.isoformat(),
            'date_to': self.date_to.isoformat(),
            'duration': self.duration
        }
