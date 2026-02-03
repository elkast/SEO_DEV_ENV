"""CLI interactif pour SEO Dev Env"""
import sys
from typing import Dict, Any


def afficher_titre():
    print("\n" + "="*60)
    print(" SEO Dev Env - Créateur d'architecture Flask")
    print("   pour développeurs francophones")
    print("="*60 + "\n")


def poser_question(question: str, options: list, defaut: int = 1) -> int:
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        marqueur = "" if i == defaut else " "
        print(f"  {marqueur} {i}. {option}")
    while True:
        try:
            choix = input(f"\nVotre choix [1-{len(options)}] (défaut: {defaut}): ").strip()
            if not choix:
                return defaut - 1
            choix_int = int(choix)
            if 1 <= choix_int <= len(options):
                return choix_int - 1
            else:
                print(f" Veuillez choisir entre 1 et {len(options)}")
        except ValueError:
            print(" Veuillez entrer un nombre valide")
        except KeyboardInterrupt:
            print("\n\n Annulé")
            sys.exit(0)


def poser_question_texte(question: str, defaut: str = "") -> str:
    prompt = f"{question} (défaut: {defaut}): " if defaut else f"{question}: "
    try:
        reponse = input(prompt).strip()
        return reponse if reponse else defaut
    except KeyboardInterrupt:
        print("\n\n Annulé")
        sys.exit(0)


def confirmer(question: str, defaut: bool = True) -> bool:
    suffixe = "[O/n]" if defaut else "[o/N]"
    try:
        reponse = input(f"{question} {suffixe}: ").strip().lower()
        if not reponse:
            return defaut
        return reponse in ["o", "oui", "y", "yes"]
    except KeyboardInterrupt:
        print("\n\n Annulé")
        sys.exit(0)


def collecter_preferences() -> Dict[str, Any]:
    afficher_titre()
    preferences = {}
    
    print(" Configuration du projet")
    preferences["nom_projet"] = poser_question_texte("Nom de votre projet", "mon-projet")
    
    type_options = [
        "Apprentissage (simple, pour débuter)",
        "Application web (structure MVC complète)",
        "API professionnelle (production-ready)",
        "Startup SaaS (auth, paiement, dashboard)"
    ]
    type_choix = poser_question(" Quel type de projet ?", type_options)
    types_mapping = {0: "apprentissage", 1: "application", 2: "api", 3: "saas"}
    preferences["type_projet"] = types_mapping[type_choix]
    
    if preferences["type_projet"] in ["application", "api", "saas"]:
        db_options = [
            "SQLite (simple, fichier local)",
            "PostgreSQL (recommandé pour production)",
            "MySQL (compatible, largement utilisé)"
        ]
        db_choix = poser_question("  Quelle base de données ?", db_options,
                                   defaut=2 if preferences["type_projet"] in ["api", "saas"] else 1)
        db_mapping = {0: "sqlite", 1: "postgresql", 2: "mysql"}
        preferences["base_donnees"] = db_mapping[db_choix]
        
        if preferences["base_donnees"] == "sqlite" and preferences["type_projet"] in ["api", "saas"]:
            print("\n  ATTENTION: SQLite non recommandé pour production.")
            if not confirmer("\n   Continuer avec SQLite ?", defaut=False):
                print("\n    Passage à PostgreSQL")
                preferences["base_donnees"] = "postgresql"
        
        auth_options = [
            "Session classique (cookies Flask)",
            "JWT (tokens, pour API)",
            "OAuth2 (Google, GitHub, etc.)"
        ]
        auth_choix = poser_question(" Type d'authentification ?", auth_options,
                                     defaut=2 if preferences["type_projet"] == "api" else 1)
        auth_mapping = {0: "session", 1: "jwt", 2: "oauth"}
        preferences["auth"] = auth_mapping[auth_choix]
        
        if preferences["type_projet"] in ["api", "saas"]:
            preferences["docker"] = True
            print("\n Docker inclus automatiquement")
        else:
            preferences["docker"] = confirmer("\n Inclure Docker ?", defaut=True)
    else:
        preferences["base_donnees"] = "sqlite"
        preferences["auth"] = "session"
        preferences["docker"] = False
    
    if preferences["type_projet"] == "saas":
        preferences["stripe"] = confirmer("\n Inclure Stripe ?", defaut=True)
        preferences["email"] = confirmer(" Inclure Flask-Mail ?", defaut=True)
        preferences["celery"] = confirmer("  Inclure Celery ?", defaut=True)
    
    preferences["git"] = confirmer("\n Initialiser Git ?", defaut=True)
    return preferences


def afficher_resume(preferences: Dict[str, Any]):
    print("\n" + "="*60)
    print(" Résumé")
    print("="*60)
    print(f"\n   Projet: {preferences['nom_projet']}")
    print(f"   Type: {preferences['type_projet']}")
    if "base_donnees" in preferences:
        print(f"    Base: {preferences['base_donnees']}")
    if "auth" in preferences:
        print(f"   Auth: {preferences['auth']}")
    if preferences.get("docker"):
        print("   Docker: ")
    if preferences.get("stripe"):
        print("   Stripe: ")
    if preferences.get("email"):
        print("   Email: ")
    if preferences.get("celery"):
        print("    Celery: ")
    if preferences.get("git"):
        print("   Git: ")
    print("\n" + "="*60 + "\n")


def afficher_prochaines_etapes(nom_projet: str, type_projet: str, docker: bool = False):
    print("\n" + "="*60)
    print(" Projet créé !")
    print("="*60)
    print(f"\n Prochaines étapes:\n")
    print(f"  1. cd {nom_projet}")
    if docker:
        print("  2. docker-compose up --build")
    else:
        if type_projet == "apprentissage":
            print("  2. python app.py")
        else:
            print("  2. python -m venv venv")
            print("  3. venv\\Scripts\\activate")
            print("  4. pip install -r requirements.txt")
            print("  5. seo db init")
            print("  6. seo user create")
            print("  7. seo run")
    print("\n Commandes:")
    print("   seo db init     - Initialiser la base")
    print("   seo user create - Créer un admin")
    print("   seo run         - Lancer l'app")
    print("\n" + "="*60 + "\n")
