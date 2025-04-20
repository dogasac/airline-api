class QueryFlightPassengerDTO:
    def __init__(self, flight_number, date, page=1, limit=10):
        self.flight_number = flight_number
        self.date = date
        self.page = page
        self.limit = limit
