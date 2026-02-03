"""Modèle Tâche"""
from app import db
from datetime import datetime

class Tache(db.Model):
    __tablename__ = "taches"
    
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    termine = db.Column(db.Boolean, default=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relation avec utilisateur
    user_id = db.Column(db.Integer, db.ForeignKey("utilisateurs.id"), nullable=False)
    
    def __repr__(self):
        return f"<Tache {self.titre}>"
