FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copier les requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application
COPY . .

# Exposer le port
EXPOSE 5000

# Variables d'environnement
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1

# Commande par défaut
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "run:app"]
