# app/controllers/query_flight_passenger_controller.py

from flask import Blueprint, request, jsonify
from app.dto.query_flight_passanger_dto import QueryFlightPassengerDTO
from app.services.query_flight_passanger_service import QueryFlightPassengerService
from flask_jwt_extended import jwt_required
from flasgger import swag_from

query_flight_passenger_bp = Blueprint('query_flight_passenger', __name__)

@query_flight_passenger_bp.route('/query-flight-passenger-list', methods=['GET'])
@jwt_required()  # JWT authentication required
@swag_from({
    'tags': ['Flight'],
    'parameters': [
        {
            'in': 'query',
            'name': 'flight_number',
            'required': True,
            'schema': {
                'type': 'string',
                'example': '1'
            }
        },
        {
            'in': 'query',
            'name': 'date',
            'required': True,
            'schema': {
                'type': 'string',
                'format': 'date',
                'example': '2025-04-19'
            }
        },
        {
            'in': 'query',
            'name': 'page',
            'required': False,
            'schema': {
                'type': 'integer',
                'default': 1,
                'example': 1
            }
        },
        {
            'in': 'query',
            'name': 'limit',
            'required': False,
            'schema': {
                'type': 'integer',
                'default': 10,
                'example': 10
            }
        }
    ],
    'security': [{'BearerAuth': []}],
    'responses': {
        200: {
            'description': 'A list of passengers for the specified flight',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'passengers': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'passenger_name': {'type': 'string'},
                                        'seat_number': {'type': 'integer'},
                                        'flight_date': {'type': 'string', 'format': 'date'}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Bad Request'
        },
        401: {
            'description': 'Unauthorized'
        }
    }
})
def query_flight_passenger_list():
    """
    Get a list of passengers for a given flight and date.
    """
    try:
        # Get query parameters
        flight_number = request.args.get('flight_number')
        date = request.args.get('date')  # Only date
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        # Create a DTO from the incoming query parameters
        query_dto = QueryFlightPassengerDTO(
            flight_number=flight_number,
            date=date,
            page=page,
            limit=limit
        )

        # Call the service to get the list of passengers
        result = QueryFlightPassengerService.get_passenger_list(query_dto)

        # Return the response
        if result["transaction_status"] == "success":
            return jsonify(result), 200
        else:
            return jsonify(result), 400

    except Exception as e:
        return jsonify({"transaction_status": "failed", "message": str(e)}), 400
