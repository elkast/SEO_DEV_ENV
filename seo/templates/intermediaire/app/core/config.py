"""Configuration de l'application"""
import os
from pathlib import Path

basedir = Path(__file__).resolve().parent.parent.parent

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-changez-moi"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or f"sqlite:///{basedir / 'app.db'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Configurations production ici

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
