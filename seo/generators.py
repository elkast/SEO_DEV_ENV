import os
import subprocess
import sys
import shutil
from pathlib import Path
from typing import Dict, Any
from .utils import creer_fichier, copier_dossier
from .cli import collecter_preferences, afficher_resume, afficher_prochaines_etapes

class EnvironnementGenerator:
    """Classe de base pour générer des environnements"""
    
    def __init__(self, niveau: str, type_app: str, chemin: str):
        self.niveau = niveau
        self.type_app = type_app
        self.chemin_projet = Path(chemin).resolve()
        self.packages = []
        self.template_dir = Path(__file__).parent / 'templates' / niveau
        
    def _installer_dependances(self):
        """Installe les packages nécessaires"""
        if self.packages:
            print(f"🔧 Installation des packages: {', '.join(self.packages)}")
            subprocess.run([sys.executable, '-m', 'pip', 'install'] + self.packages)
        
    def _copier_template(self):
        """Copie les fichiers du template"""
        if self.template_dir.exists():
            copier_dossier(self.template_dir, self.chemin_projet)
        else:
            print(f"⚠️ Avertissement: Template {self.niveau} non trouvé, création de base")
            self._creer_structure_base()
    
    def _creer_structure_base(self):
        """Crée une structure de base si le template est manquant"""
        creer_fichier(self.chemin_projet / 'app.py', "# Votre application Flask")
        (self.chemin_projet / 'templates').mkdir(exist_ok=True)
        creer_fichier(self.chemin_projet / 'templates/index.html', "<h1>Bienvenue</h1>")
        
    def _post_creation(self):
        """Actions supplémentaires après création"""
        pass
        
    def generer(self):
        """Méthode principale pour générer l'environnement"""
        self.chemin_projet.mkdir(exist_ok=True, parents=True)
        print(f"🏗️ Création de l'environnement {self.niveau} ({self.type_app})...")
        
        self._copier_template()
        self._creer_structure()
        self._installer_dependances()
        self._post_creation()
        
        print(f"✅ Environnement créé avec succès dans {self.chemin_projet}")
        print("👉 Pour démarrer: cd " + str(self.chemin_projet))

class DebutantWebGenerator(EnvironnementGenerator):
    """Générateur pour débutants - Site web simple"""
    
    def __init__(self, chemin):
        super().__init__('debutant', 'web', chemin)
        self.packages = ['flask', 'python-dotenv']
    
    def _creer_structure(self):
        # Personnalisation supplémentaire
        creer_fichier(
            self.chemin_projet / 'README.md',
            f"# Mon Premier Projet Flask\n\nCe projet a été créé avec SEO pour les débutants!"
        )

class IntermediaireWebGenerator(EnvironnementGenerator):
    """Générateur intermédiaire - Applications web complètes"""
    
    def __init__(self, chemin):
        super().__init__('intermediaire', 'web', chemin)
        self.packages = [
            'flask',
            'flask-sqlalchemy',
            'flask-wtf',
            'flask-login',
            'flask-migrate',
            'python-dotenv'
        ]
    
    def _creer_structure(self):
        # Création de la base de données
        db_path = self.chemin_projet / 'app.db'
        if not db_path.exists():
            with open(db_path, 'w') as f:
                f.write("")
        
        # Création du fichier requirements
        creer_fichier(
            self.chemin_projet / 'requirements.txt',
            "\n".join(self.packages)
        )

class ProWebGenerator(EnvironnementGenerator):
    """Générateur pro - Applications professionnelles"""
    
    def __init__(self, chemin):
        super().__init__('pro', 'web', chemin)
        self.packages = [
            'flask',
            'flask-restx',
            'flask-cors',
            'flask-sqlalchemy',
            'flask-migrate',
            'flask-jwt-extended',
            'python-dotenv',
            'gunicorn',
            'psycopg2-binary'
        ]
    
    def _post_creation(self):
        # Initialiser un dépôt Git
        try:
            subprocess.run(['git', 'init', str(self.chemin_projet)], check=True)
            print("📦 Dépôt Git initialisé")
        except:
            print("⚠️ Git non installé, ignore l'initialisation du dépôt")

# Interface simplifiée
def creer_environnement(niveau, type_app='web', chemin='.'):
    """
    Crée un environnement de développement adapté
    
    Args:
        niveau: 'debutant', 'intermediaire' ou 'pro'
        type_app: 'web' ou 'mobile' (défaut: 'web')
        chemin: Chemin où créer le projet (défaut: dossier actuel)
    """
    generators = {
        'debutant': DebutantWebGenerator,
        'intermediaire': IntermediaireWebGenerator,
        'pro': ProWebGenerator
    }
    
    if niveau not in generators:
        raise ValueError(f"🚫 Niveau non supporté: {niveau}")
    
    generator = generators[niveau](chemin)
    generator.generer()
    
    # Ajout des instructions spécifiques
    if niveau == 'debutant':
        print("\n🚀 Pour démarrer votre application:")
        print(f"cd {chemin}")
        print("python app.py")
    elif niveau == 'intermediaire':
        print("\n🚀 Pour initialiser la base de données:")
        print(f"cd {chemin}")
        print("flask db init")
        print("flask db migrate")
        print("flask db upgrade")
        print("flask run")
    else:
        print("\n🚀 Pour démarrer avec Docker:")
        print(f"cd {chemin}")
        print("docker-compose up --build")

# Alias pour une utilisation plus simple
creer_projet = creer_environnement


def main():
    """Point d'entrée principal pour le CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='SEO Dev Env - Générateur de projets Flask pour francophones'
    )
    
    subparsers = parser.add_subparsers(dest='commande', help='Commandes disponibles')
    
    # Commande create (mode interactif)
    parser_create = subparsers.add_parser('create', help='Créer un nouveau projet (mode interactif)')
    parser_create.add_argument('nom', nargs='?', help='Nom du projet (optionnel, sera demandé si non fourni)')
    
    # Commandes db
    parser_db = subparsers.add_parser('db', help='Gestion de la base de données')
    parser_db.add_argument('action', choices=['init', 'migrate', 'upgrade', 'downgrade'])
    
    # Commandes user
    parser_user = subparsers.add_parser('user', help='Gestion des utilisateurs')
    parser_user.add_argument('action', choices=['create', 'list'])
    
    # Commande run
    parser_run = subparsers.add_parser('run', help='Lancer l\'application')
    parser_run.add_argument('mode', nargs='?', default='dev', choices=['dev', 'prod'])
    
    # Commande help
    parser_help = subparsers.add_parser('help', help='Afficher l\'aide')
    
    args = parser.parse_args()
    
    # Si aucune commande, afficher l'aide
    if not args.commande:
        from .commandes import afficher_aide
        afficher_aide()
        return
    
    # Traiter les commandes
    if args.commande == 'create':
        creer_projet_interactif(args.nom)
    
    elif args.commande == 'db':
        from .commandes import commande_db
        commande_db(args.action)
    
    elif args.commande == 'user':
        from .commandes import commande_user
        commande_user(args.action)
    
    elif args.commande == 'run':
        from .commandes import commande_run
        commande_run(args.mode)
    
    elif args.commande == 'help':
        from .commandes import afficher_aide
        afficher_aide()


def creer_projet_interactif(nom_fourni: str = None):
    """Crée un projet en mode interactif"""
    # Collecter les préférences
    preferences = collecter_preferences()
    
    # Utiliser le nom fourni en argument si disponible
    if nom_fourni:
        preferences['nom_projet'] = nom_fourni
    
    # Afficher le résumé
    afficher_resume(preferences)
    
    # Confirmer
    from .cli import confirmer
    if not confirmer("Créer le projet avec cette configuration ?"):
        print("❌ Annulé")
        return
    
    # Générer le projet selon le type
    generer_selon_preferences(preferences)
    
    # Afficher les prochaines étapes
    afficher_prochaines_etapes(
        preferences['nom_projet'],
        preferences['type_projet'],
        preferences.get('docker', False)
    )


def generer_selon_preferences(preferences: Dict[str, Any]):
    """Génère le projet selon les préférences"""
    type_projet = preferences['type_projet']
    nom_projet = preferences['nom_projet']
    
    if type_projet == 'apprentissage':
        generator = ApprentissageGenerator(nom_projet, preferences)
    elif type_projet == 'application':
        generator = ApplicationGenerator(nom_projet, preferences)
    elif type_projet == 'api':
        generator = APIGenerator(nom_projet, preferences)
    elif type_projet == 'saas':
        generator = SaaSGenerator(nom_projet, preferences)
    else:
        raise ValueError(f"Type de projet inconnu: {type_projet}")
    
    generator.generer()


class ApprentissageGenerator(EnvironnementGenerator):
    """Générateur pour débutants"""
    def __init__(self, nom: str, preferences: Dict[str, Any]):
        super().__init__('debutant', 'web', nom)
        self.preferences = preferences
        self.packages = ['flask', 'python-dotenv']
    
    def _creer_structure(self):
        creer_fichier(self.chemin_projet / 'README.md',
                     f"# {self.preferences['nom_projet']}\n\nProjet Flask pour apprentissage")


class ApplicationGenerator(EnvironnementGenerator):
    """Générateur pour applications web (architecture par feature)"""
    def __init__(self, nom: str, preferences: Dict[str, Any]):
        super().__init__('intermediaire', 'web', nom)
        self.preferences = preferences
        self.packages = [
            'flask', 'flask-sqlalchemy', 'flask-migrate',
            'flask-wtf', 'flask-login', 'python-dotenv'
        ]
    
    def _creer_structure(self):
        creer_fichier(self.chemin_projet / 'requirements.txt', "\n".join(self.packages))


class APIGenerator(EnvironnementGenerator):
    """Générateur pour API professionnelles"""
    def __init__(self, nom: str, preferences: Dict[str, Any]):
        super().__init__('pro', 'api', nom)
        self.preferences = preferences
        self.packages = [
            'flask', 'flask-restx', 'flask-cors', 'flask-sqlalchemy',
            'flask-migrate', 'flask-jwt-extended', 'python-dotenv', 'gunicorn'
        ]
        if preferences.get('base_donnees') == 'postgresql':
            self.packages.append('psycopg2-binary')
        elif preferences.get('base_donnees') == 'mysql':
            self.packages.append('pymysql')
    
    def _creer_structure(self):
        creer_fichier(self.chemin_projet / 'requirements.txt', "\n".join(self.packages))


class SaaSGenerator(EnvironnementGenerator):
    """Générateur pour startup SaaS"""
    def __init__(self, nom: str, preferences: Dict[str, Any]):
        super().__init__('pro', 'saas', nom)
        self.preferences = preferences
        self.packages = [
            'flask', 'flask-restx', 'flask-cors', 'flask-sqlalchemy',
            'flask-migrate', 'flask-jwt-extended', 'python-dotenv', 'gunicorn'
        ]
        if preferences.get('stripe'):
            self.packages.append('stripe')
        if preferences.get('email'):
            self.packages.append('flask-mail')
        if preferences.get('celery'):
            self.packages.extend(['celery', 'redis'])
        if preferences.get('base_donnees') == 'postgresql':
            self.packages.append('psycopg2-binary')
    
    def _creer_structure(self):
        creer_fichier(self.chemin_projet / 'requirements.txt', "\n".join(self.packages))