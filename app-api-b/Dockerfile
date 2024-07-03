# Utiliser l'image Python officielle comme base
FROM python:3.9-slim-buster

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/requirements.txt

# Installer les dépendances nécessaires
RUN pip install -r /app/requirements.txt

# Copier le code de l'API dans le conteneur
COPY . /app

# Exposer le port de l'API
EXPOSE 80

# Démarrer l'API
CMD ["python", "/app/api_b.py"]
