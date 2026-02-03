# 🚀 Guide d'Utilisation Rapide - SEO Dev Env v2.0

## Installation

```bash
# 1. Installer le package
pip install -e .

# 2. Vérifier l'installation
seo --help
```

## Utilisation

### Mode Interactif (Recommandé)

```bash
seo create
```

Vous serez guidé avec des questions :

```
🚀 SEO Dev Env - Créateur d'architecture Flask
   pour développeurs francophones
============================================================

📦 Configuration du projet
Nom de votre projet (défaut: mon-projet): ma-super-app

🎯 Quel type de projet voulez-vous créer ?
  → 1. Apprentissage (simple, pour débuter)
    2. Application web (structure MVC complète)
    3. API professionnelle (production-ready)
    4. Startup SaaS (auth, paiement, dashboard)

Votre choix [1-4] (défaut: 1): 2

🗄️  Quelle base de données voulez-vous utiliser ?
    1. SQLite (simple, fichier local)
  → 2. PostgreSQL (recommandé pour production)
    3. MySQL (compatible, largement utilisé)

Votre choix [1-3] (défaut: 2): 2

🔐 Quel type d'authentification ?
  → 1. Session classique (cookies Flask)
    2. JWT (tokens, pour API)
    3. OAuth2 (Google, GitHub, etc.)

Votre choix [1-3] (défaut: 1): 1

🐳 Voulez-vous inclure Docker ? [O/n]: o

📦 Initialiser un dépôt Git ? [O/n]: o
```

### Commandes Disponibles

#### 📦 Création de Projet
```bash
seo create                    # Mode interactif
seo create mon-projet         # Avec nom prédéfini
```

#### 🗄️ Gestion Base de Données
```bash
seo db init                   # Initialiser la base
seo db migrate                # Créer une migration
seo db upgrade                # Appliquer les migrations
seo db downgrade              # Annuler la dernière migration
```

#### 👤 Gestion Utilisateurs
```bash
seo user create               # Créer un admin
seo user list                 # Lister les utilisateurs
```

#### 🚀 Lancement
```bash
seo run                       # Mode développement
seo run prod                  # Mode production
```

#### 🛠️ Autres
```bash
seo test                      # Lancer les tests
seo shell                     # Shell Flask interactif
seo --help                    # Aide complète
```

## Exemples d'Utilisation

### Exemple 1 : Application Simple (Apprentissage)

```bash
# 1. Créer le projet
seo create

# Choisir :
# - Type : 1 (Apprentissage)
# - Nom : mon-premier-projet

# 2. Lancer
cd mon-premier-projet
python app.py

# 3. Ouvrir http://localhost:5000
```

### Exemple 2 : Application Web avec Auth

```bash
# 1. Créer le projet
seo create

# Choisir :
# - Type : 2 (Application web)
# - Base : PostgreSQL
# - Auth : Session
# - Docker : Oui

# 2. Avec Docker
cd mon-app
docker-compose up --build

# 3. OU sans Docker
cd mon-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
seo db init
seo db migrate
seo user create
seo run

# 4. Ouvrir http://localhost:5000
```

### Exemple 3 : API Professionnelle

```bash
# 1. Créer le projet
seo create

# Choisir :
# - Type : 3 (API professionnelle)
# - Base : PostgreSQL
# - Auth : JWT
# - Docker : Oui (automatique)

# 2. Lancer
cd mon-api
docker-compose up --build

# 3. Documentation Swagger disponible sur :
# http://localhost:5000/api/docs
```

### Exemple 4 : Startup SaaS Complète

```bash
# 1. Créer le projet
seo create

# Choisir :
# - Type : 4 (Startup SaaS)
# - Base : PostgreSQL
# - Auth : JWT
# - Stripe : Oui
# - Email : Oui
# - Celery : Oui
# - Docker : Oui (automatique)

# 2. Lancer
cd mon-saas
docker-compose up --build

# Vous obtenez :
# - API REST avec Swagger
# - Authentification JWT
# - Paiements Stripe
# - Envoi d'emails
# - Tâches asynchrones
# - Dashboard admin
```

## Architecture des Projets

### Type 1 : Apprentissage
```
mon-projet/
├── app.py              # Application Flask simple
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

### Type 2 : Application (Architecture par Feature)
```
mon-app/
├── app/
│   ├── __init__.py
│   ├── core/           # Configuration
│   │   ├── config.py
│   │   └── __init__.py
│   ├── utilisateurs/   # Feature utilisateurs
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── __init__.py
│   └── taches/         # Feature tâches
│       ├── models.py
│       ├── routes.py
│       └── __init__.py
├── run.py
├── config.py
├── requirements.txt
├── docker-compose.yml
└── .env.example
```

### Type 3 : API
```
mon-api/
├── app/
│   ├── api/            # Routes API
│   ├── core/           # Config
│   ├── db/             # Modèles
│   └── services/       # Logique métier
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Type 4 : SaaS
```
mon-saas/
├── app/
│   ├── api/
│   ├── auth/           # Authentification
│   ├── paiements/      # Stripe
│   ├── emails/         # Flask-Mail
│   ├── tasks/          # Celery
│   └── admin/          # Dashboard
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Avertissements Intelligents

L'outil vous guide pour éviter les erreurs :

### SQLite en Production
```
⚠️  ATTENTION: SQLite n'est pas recommandé pour la production.
   Raisons: pas de concurrence, limite de performance

   Voulez-vous continuer avec SQLite ? [o/N]: 
```

### Docker Automatique
```
🐳 Docker sera inclus automatiquement (recommandé pour ce type de projet)
```

## Workflow Complet

```bash
# 1. Création
seo create

# 2. Configuration
cd mon-projet
cp .env.example .env
# Éditer .env avec vos clés

# 3. Installation (sans Docker)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 4. Base de données
seo db init
seo db migrate

# 5. Créer un admin
seo user create

# 6. Lancer
seo run

# 7. Tests
seo test

# 8. Production
seo run prod
# OU
docker-compose up --build
```

## Commandes Utiles

```bash
# Shell interactif Flask
seo shell

# Migration avec message
seo db migrate -m "Ajout table produits"

# Voir l'aide
seo --help
seo db --help
seo user --help
```

## Conseils

1. **Débutant** : Commencez avec type 1 (Apprentissage)
2. **Projet sérieux** : Utilisez type 2 (Application) avec PostgreSQL
3. **API** : Type 3 avec JWT et Docker
4. **Startup** : Type 4 avec toutes les fonctionnalités

## Problèmes Courants

### Erreur : commande 'seo' non trouvée
```bash
# Solution : Réinstaller
pip install -e .
```

### Erreur : Cannot import 'app'
```bash
# Solution : Vérifier que vous êtes dans le bon dossier
cd mon-projet
```

### Docker ne démarre pas
```bash
# Solution : Vérifier docker-compose
docker-compose ps
docker-compose logs
```

## Support

- **Documentation** : README_NOUVEAU.md
- **Architecture** : Voir les templates dans seo/templates/
- **Issues** : GitHub Issues

---

**Créé avec ❤️ pour les développeurs francophones**
