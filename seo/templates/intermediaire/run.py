"""Point d'entrée pour lancer l'application"""
import os
from app import create_app, db
from app.utilisateurs.models import User
from app.taches.models import Tache

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Tache": Tache}

if __name__ == "__main__":
    print(" Application Flask démarrée")
    print("   Architecture par feature (domain-based)")
    print("   http://localhost:5000")
    app.run(debug=True)
