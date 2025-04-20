from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from app.services.flight_service import add_flight, query_flights

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/add-flight', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Flight'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'date_from': {'type': 'string', 'format': 'date'},
                    'date_to': {'type': 'string', 'format': 'date'},
                    'airport_from': {'type': 'string'},
                    'airport_to': {'type': 'string'},
                    'duration': {'type': 'integer'},
                    'capacity': {'type': 'integer'}
                },
                'required': ['date_from', 'date_to', 'airport_from', 'airport_to', 'duration', 'capacity']
            }
        }
    ],
    'security': [{'BearerAuth': []}],
    'responses': {
        201: {'description': 'Flight successfully added'},
        400: {'description': 'Bad Request'}
    }
})
def add_flight_route():
    """
    Add a new flight to the airline schedule
    """
    data = request.get_json()
    result = add_flight(data)

    if result["transaction_status"] == "success":
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@flight_bp.route('/query-flight', methods=['GET'])
@swag_from({
    'tags': ['Flight'],
    'parameters': [
        {'in': 'query', 'name': 'date_from', 'required': True, 'type': 'string', 'format': 'date', 'example': '2025-04-19'},
        {'in': 'query', 'name': 'date_to', 'required': True, 'type': 'string', 'format': 'date', 'example': '2025-04-19'},
        {'in': 'query', 'name': 'airport_from', 'required': True, 'type': 'string', 'example': 'IST'},
        {'in': 'query', 'name': 'airport_to', 'required': True, 'type': 'string', 'example': 'IZM'},
        {'in': 'query', 'name': 'number_of_people', 'required': True, 'type': 'integer', 'example': '1'},
        {'in': 'query', 'name': 'trip_type', 'required': True, 'type': 'string', 'enum': ['one-way', 'round-trip']}
    ],
    'responses': {
        200: {'description': 'Available flights successfully retrieved'},
        400: {'description': 'Bad Request'}
    }
})
def query_flight_route():
    """
    Query available flights based on date range, airports, number of people, and trip type
    """
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    airport_from = request.args.get('airport_from')
    airport_to = request.args.get('airport_to')
    number_of_people = int(request.args.get('number_of_people'))
    trip_type = request.args.get('trip_type')

    result = query_flights(date_from, date_to, airport_from, airport_to, number_of_people, trip_type)

    if "flights" in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400
