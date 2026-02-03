# 🚀 SEO Dev Env - Générateur Flask pour Francophones

> Créez des applications Flask professionnelles en quelques secondes avec un CLI interactif en français

## ✨ Nouveautés Version 2.0

### 🎯 CLI Interactif Intelligent
- Questions guidées pour configurer votre projet
- Choix intelligents selon le type de projet
- Avertissements pour éviter les mauvaises décisions
- Support complet en français

### 🏗️ Architecture Moderne par Feature
Au lieu de :
```
app/
  models.py      # TOUT dans un fichier
  routes.py      # Devient ingérable après 6 mois
```

Vous obtenez :
```
app/
  core/          # Configuration, extensions
  utilisateurs/  # Feature utilisateurs
    models.py
    routes.py
    service.py
  taches/        # Feature tâches
    models.py
    routes.py
    service.py
```

**Avantages** : Code organisé, facile à maintenir, scalable

### ⚙️ Commandes Internes (Nouveau!)
```bash
seo db init        # Initialiser la base
seo db migrate     # Créer une migration
seo user create    # Créer un admin
seo run            # Lancer l'app
```

Plus besoin de mémoriser les commandes Flask complexes !

### 🎨 4 Types de Projets

#### 1. Apprentissage 🐣
Pour débuter avec Flask
- Structure simple
- Exemples commentés
- Prêt en 30 secondes

```bash
seo create
# Choisir option 1
```

#### 2. Application Web ⚡
Structure MVC complète avec architecture par feature
- Organisation professionnelle
- Auth intégrée
- Base de données configurée

```bash
seo create
# Choisir option 2
```

#### 3. API Professionnelle 🚀
API REST production-ready
- Flask-RESTX intégré
- JWT ou OAuth2
- Docker inclus
- Documentation Swagger auto

```bash
seo create
# Choisir option 3
```

#### 4. Startup SaaS 💼
Application complète avec :
- ✅ Authentification (JWT/OAuth)
- ✅ Paiements (Stripe)
- ✅ Envoi d'emails
- ✅ Tâches asynchrones (Celery)
- ✅ Dashboard admin
- ✅ Docker + PostgreSQL

```bash
seo create
# Choisir option 4
```

## 📦 Installation

```bash
pip install seo-dev-env
```

## 🎯 Utilisation Rapide

### Mode Interactif (Recommandé)
```bash
seo create
```

L'outil vous guidera avec des questions :
1. Nom du projet ?
2. Type de projet ? (Apprentissage / Application / API / SaaS)
3. Quelle base de données ? (SQLite / PostgreSQL / MySQL)
4. Type d'authentification ? (Session / JWT / OAuth2)
5. Inclure Docker ?
6. Options supplémentaires (Stripe, Email, Celery...)

### Mode Direct
```bash
seo create mon-super-projet
```

### Ancien Mode (Compatible)
```bash
from seo import creer_projet
creer_projet('application', 'mon-projet')
```

## 🛠️ Commandes Disponibles

### Gestion de Base de Données
```bash
seo db init        # Initialiser la base
seo db migrate     # Créer une migration  
seo db upgrade     # Appliquer les migrations
seo db downgrade   # Annuler la dernière migration
```

### Gestion des Utilisateurs
```bash
seo user create    # Créer un utilisateur admin
seo user list      # Lister les utilisateurs
```

### Lancement
```bash
seo run            # Mode développement (debug activé)
seo run prod       # Mode production (avec gunicorn)
```

### Autres
```bash
seo test           # Lancer les tests
seo shell          # Shell Flask interactif
seo --help         # Voir toutes les commandes
```

## 🎨 Exemple Complet

```bash
# 1. Créer le projet
seo create

# Répondre aux questions :
# - Nom : gestion-taches
# - Type : Application web
# - Base : PostgreSQL
# - Auth : Session
# - Docker : Oui

# 2. Entrer dans le projet
cd gestion-taches

# 3. Avec Docker (recommandé)
docker-compose up --build

# OU sans Docker

# 3. Créer environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Initialiser la base
seo db init
seo db migrate

# 6. Créer un admin
seo user create

# 7. Lancer l'application
seo run

# 🎉 Application disponible sur http://localhost:5000
```

## 🏗️ Architecture par Feature (Nouveau!)

### Avant (Structure classique)
```
app/
  models.py          # 500 lignes, tout mélangé
  routes.py          # 800 lignes, impossible à maintenir
  forms.py           # 300 lignes
```

### Après (Architecture moderne)
```
app/
  core/
    __init__.py
    config.py         # Configuration centralisée
    extensions.py     # Extensions Flask
  
  utilisateurs/       # Feature complète
    __init__.py
    models.py         # Modèle User
    routes.py         # Routes auth
    service.py        # Logique métier
    schema.py         # Validation
  
  taches/             # Feature complète
    __init__.py
    models.py         # Modèle Tache
    routes.py         # Routes CRUD
    service.py        # Logique métier
  
  paiements/          # Feature SaaS
    __init__.py
    models.py
    routes.py
    stripe_service.py
```

**Avantages** :
- ✅ Chaque feature est isolée
- ✅ Facile à tester
- ✅ Scalable (ajoutez des features sans toucher le reste)
- ✅ Équipes peuvent travailler en parallèle
- ✅ Code réutilisable

## 🐳 Docker Inclus

Pour API et SaaS, Docker est inclus automatiquement :

```yaml
# docker-compose.yml généré automatiquement
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: app_db
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

Lancement :
```bash
docker-compose up --build
```

## ⚠️ Avertissements Intelligents

L'outil vous prévient des mauvaises décisions :

### Exemple : SQLite en Production
```
⚠️  ATTENTION: SQLite n'est pas recommandé pour la production.
   Raisons: pas de concurrence, limite de performance

   Voulez-vous continuer avec SQLite ? [o/N]: n

   → Passage à PostgreSQL (recommandé)
```

## 🎯 Cas d'Usage

### Débutant qui apprend Flask
```bash
seo create
# Option 1 : Apprentissage
# 30 secondes plus tard, vous codez !
```

### Développeur qui veut un blog
```bash
seo create
# Option 2 : Application web
# Architecture propre, auth incluse
```

### Startup qui lance une API
```bash
seo create
# Option 3 : API professionnelle
# Swagger, JWT, Docker, PostgreSQL
```

### Entrepreneur qui lance un SaaS
```bash
seo create
# Option 4 : Startup SaaS
# Stripe, emails, Celery, dashboard admin
```

## 🆚 Comparaison

| Feature | SEO Dev Env v1 | SEO Dev Env v2 |
|---------|----------------|----------------|
| CLI | Ligne de commande | **Interactif** |
| Architecture | MVC classique | **Par feature** |
| Commandes | Flask natif | **Commandes simplifiées** |
| Avertissements | ❌ | **✅ Intelligents** |
| Docker | Manuel | **✅ Auto pour API/SaaS** |
| Templates | 3 niveaux | **4 types + options** |
| SaaS | ❌ | **✅ Stripe, Email, Celery** |

## 🔥 Ce qui Rend cet Outil Unique

1. **Premier générateur Flask 100% français**
2. **Architecture par feature** (moderne, scalable)
3. **Commandes internes** (plus simple que Flask CLI)
4. **Avertissements intelligents** (évite les erreurs de débutant)
5. **Mode SaaS complet** (Stripe + Email + Celery inclus)
6. **Docker par défaut** pour production

## 📚 Documentation

- [Guide d'architecture](./docs/ARCHITECTURE.md)
- [Guide Docker](./docs/DOCKER.md)
- [Guide SaaS](./docs/SAAS.md)
- [FAQ](./docs/FAQ.md)

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

MIT

## 👤 Auteur

**SEO Dev Env Team**

## 🙏 Remerciements

Merci à tous les développeurs francophones qui nous ont fait confiance !

---

**Créé avec ❤️ pour la communauté francophone**
