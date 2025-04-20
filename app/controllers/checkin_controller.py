from flask import Blueprint, request, jsonify
from app.dto.checkin_dto import CheckinDTO
from app.services.checkin_service import CheckinService
from flasgger import swag_from

checkin_bp = Blueprint('checkin', __name__)

@checkin_bp.route('/checkin', methods=['POST'])
@swag_from({
    'tags': ['Checkin'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'flight_number': {'type': 'integer'},
                    'date': {'type': 'string', 'format': 'date'},
                    'passenger_name': {'type': 'string'}
                },
                'required': ['flight_number', 'date', 'passenger_name']
            }
        }
    ],
    'responses': {
        200: {'description': 'Checkin successful'},
        400: {'description': 'Bad request'}
    }
})
def checkin_flight():
    """
    Check in a passenger to a flight and assign a seat
    """
    try:
        data = request.get_json()

        # Create a DTO from the incoming data
        checkin_dto = CheckinDTO(
            flight_number=data.get('flight_number'),
            date=data.get('date'),
            passenger_name=data.get('passenger_name')
        )

        # Call the CheckinService to process the check-in
        result = CheckinService.checkin_passenger(checkin_dto)

        # Return the response based on the result
        if result["transaction_status"] == "success":
            return jsonify(result), 200
        else:
            return jsonify(result), 400

    except Exception as e:
        return jsonify({"transaction_status": "failed", "message": str(e)}), 400
