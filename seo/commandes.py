"""
Commandes internes pour gérer le projet Flask
"""
import os
import sys
import subprocess
from pathlib import Path


def commande_db(action: str):
    """Gestion de la base de données"""
    if action == "init":
        print("  Initialisation de la base...")
        subprocess.run([sys.executable, "-m", "flask", "db", "init"])
        print(" Base initialisée")
    elif action == "migrate":
        message = input("Message (optionnel): ").strip()
        if message:
            subprocess.run([sys.executable, "-m", "flask", "db", "migrate", "-m", message])
        else:
            subprocess.run([sys.executable, "-m", "flask", "db", "migrate"])
        print(" Migration créée")
    elif action == "upgrade":
        subprocess.run([sys.executable, "-m", "flask", "db", "upgrade"])
        print(" Migrations appliquées")
    else:
        print(f" Action '{action}' inconnue")


def commande_user(action: str):
    """Gestion des utilisateurs"""
    if action == "create":
        print(" Création admin\n")
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        import getpass
        password = getpass.getpass("Password: ")
        
        try:
            from app import create_app, db
            from app.models import User
            app = create_app()
            with app.app_context():
                user = User(username=username, email=email, is_admin=True)
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                print(f" Utilisateur '{username}' créé")
        except ImportError as e:
            print(f" Erreur: {e}")
    elif action == "list":
        try:
            from app import create_app, db
            from app.models import User
            app = create_app()
            with app.app_context():
                users = User.query.all()
                print("\n Utilisateurs:\n")
                for user in users:
                    print(f"   {user.username}")
        except ImportError:
            print(" Impossible de charger les utilisateurs")


def commande_run(mode: str = "dev"):
    """Lance l'application"""
    if mode == "dev":
        print(" Mode développement...\n")
        os.environ["FLASK_ENV"] = "development"
        os.environ["FLASK_DEBUG"] = "1"
        if Path("run.py").exists():
            subprocess.run([sys.executable, "run.py"])
        elif Path("app.py").exists():
            subprocess.run([sys.executable, "app.py"])
        else:
            subprocess.run([sys.executable, "-m", "flask", "run", "--debug"])


def afficher_aide():
    """Affiche l'aide"""
    print("\n" + "="*60)
    print(" Commandes SEO")
    print("="*60 + "\n")
    print("  Base de données:")
    print("  seo db init      - Initialiser")
    print("  seo db migrate   - Créer migration")
    print("  seo db upgrade   - Appliquer")
    print("\n Utilisateurs:")
    print("  seo user create  - Créer admin")
    print("  seo user list    - Lister")
    print("\n Lancement:")
    print("  seo run          - Mode dev")
    print("\n" + "="*60 + "\n")
