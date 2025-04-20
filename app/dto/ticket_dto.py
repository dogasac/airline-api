class TicketRequestDTO:
    def __init__(self, flight_number, date, passenger_names):
        self.flight_number = flight_number
        self.date = date
        self.passenger_names = passenger_names

class TicketResponseDTO:
    def __init__(self, transaction_status, ticket_numbers, remaining_capacity):
        self.transaction_status = transaction_status
        self.ticket_numbers = ticket_numbers
        self.remaining_capacity = remaining_capacity

    def to_dict(self):
        return {
            'transaction_status': self.transaction_status,
            'ticket_numbers': self.ticket_numbers,
            'remaining_capacity': self.remaining_capacity
        }
