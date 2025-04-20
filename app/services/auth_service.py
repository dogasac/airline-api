from app.models.user import User
from app.dto.user_dto import LoginDTO
from flask_jwt_extended import create_access_token

def login_user(login_dto: LoginDTO):
    user = User.query.filter_by(username=login_dto.username).first()
    if user and user.password == login_dto.password:  # Parola hashing kullanmak istersen `check_password_hash` ile değiştirilebilir
        token = create_access_token(identity=user.username)
        return {
            'transaction_status': 'success',
            'message': 'Login successful',
            'token': token
        }
    else:
        return {
            'transaction_status': 'failed',
            'message': 'Invalid credentials'
        }
