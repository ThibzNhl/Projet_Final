# Dockerfile
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut (à modifier pour tests)
CMD ["python", "manage.py", "test"]
