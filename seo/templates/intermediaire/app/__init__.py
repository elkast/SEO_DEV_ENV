"""
Point d'entrée de l'application
Architecture par feature (domain-based)
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .core.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "utilisateurs.connexion"
login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Enregistrer les blueprints (features)
    from app.utilisateurs.routes import bp as utilisateurs_bp
    from app.taches.routes import bp as taches_bp
    
    app.register_blueprint(utilisateurs_bp)
    app.register_blueprint(taches_bp)
    
    # Route racine
    @app.route("/")
    def index():
        return "Application Flask - Architecture par feature"
    
    return app
