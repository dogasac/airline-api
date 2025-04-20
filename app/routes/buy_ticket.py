# app/routes/buy_ticket_route.py

from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from app.services.ticket_service import TicketService
from app.dto.ticket_dto import TicketRequestDTO, TicketResponseDTO

buy_ticket_bp = Blueprint('buy_ticket', __name__)

@buy_ticket_bp.route('/buy-ticket', methods=['POST'])
@jwt_required()  # Authentication is required
@swag_from({
    'tags': ['Ticket'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'flight_number': {'type': 'string'},
                    'date': {'type': 'string', 'format': 'date'},  # Adjusted to 'date' format
                    'passenger_names': {
                        'type': 'array',
                        'items': {'type': 'string'}
                    }
                },
                'required': ['flight_number', 'date', 'passenger_names']
            }
        }
    ],
    'security': [
        {
            'BearerAuth': []
        }
    ],
    'responses': {
        200: {'description': 'Ticket successfully purchased'},
        400: {'description': 'Bad Request'},
        404: {'description': 'Flight not found or sold out'}
    }
})
def buy_ticket():
    """
    Buy a ticket for a flight and decrease the available capacity
    """
    data = request.get_json()

    flight_number = data.get('flight_number')
    flight_date_str = data.get('date')  # Expecting 'date' in the format 'YYYY-MM-DD'
    passenger_names = data.get('passenger_names')

    if not flight_number or not flight_date_str or not passenger_names:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create DTO
    ticket_request = TicketRequestDTO(flight_number, flight_date_str, passenger_names)

    # Call the service layer
    result, status_code = TicketService.buy_ticket(
        ticket_request.flight_number,
        ticket_request.date,
        ticket_request.passenger_names
    )

    if status_code == 200:
        # Convert to DTO Response and return it
        ticket_response = TicketResponseDTO(
            result['transaction_status'],
            result['ticket_numbers'],
            result['remaining_capacity']
        )
        return jsonify(ticket_response.to_dict()), 200
    else:
        return jsonify(result), status_code
