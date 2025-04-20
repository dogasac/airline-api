from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.auth_service import login_user
from app.dto.user_dto import LoginDTO

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Authentication'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['username', 'password']
            }
        }
    ],
    'responses': {
        200: {'description': 'Login successful'},
        401: {'description': 'Invalid credentials'}
    }
})
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'transaction_status': 'failed', 'message': 'Missing username or password'}), 400

    login_dto = LoginDTO(username=data['username'], password=data['password'])
    result = login_user(login_dto)

    status_code = 200 if result['transaction_status'] == 'success' else 401
    return jsonify(result), status_code
