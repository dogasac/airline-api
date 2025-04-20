from flask import Flask
from flasgger import Swagger
from app.extensions import db, jwt  # Buradan db ve jwt'i alıyoruz
from app.controllers.auth import auth_bp
from app.controllers.flight_controller import flight_bp
from app.routes.buy_ticket import buy_ticket_bp  # buy_ticket route'u burada import ediliyor
from app.controllers.checkin_controller import checkin_bp
from app.controllers.query_flight_controller import query_flight_passenger_bp
import os
from config import Config 


def create_app():
    app = Flask(__name__)
    
    # Config ayarlarını yükle
    app.config.from_object(Config) # Config sınıfından ayarları alıyoruz

    # Swagger yapılandırması
    app.config['SWAGGER'] = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "swagger_ui": True,
        "specs_route": "/swagger/",
        "securityDefinitions": {
            "BearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        },
        "security": [{"BearerAuth": []}],
    }

    # Swagger'ı burada başlatıyoruz
    Swagger(app)

    db.init_app(app)  # Veritabanını başlatıyoruz
    jwt.init_app(app)  # JWT'i başlatıyoruz

    # Blueprint'leri kaydediyoruz
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(flight_bp, url_prefix='/api/v1/flight')
    app.register_blueprint(buy_ticket_bp, url_prefix='/api/v1/ticket') 
    app.register_blueprint(checkin_bp, url_prefix='/api/v1')
    app.register_blueprint(query_flight_passenger_bp, url_prefix='/api/v1')



    return app
