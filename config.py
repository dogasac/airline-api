import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # .env dosyasını yükler

class Config:
    # Çevresel değişkenlerden veritabanı URL'si
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # .env dosyasındaki DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy değişiklik izlemeyi devre dışı bırakıyoruz
    SECRET_KEY = os.getenv("SECRET_KEY")  # Uygulama için gizli anahtar
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")  # JWT için gizli anahtar
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Erişim token'ının geçerlilik süresi (saniye cinsinden)
