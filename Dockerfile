# Dockerfile
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port que Django utilise
EXPOSE 8000

# Étape 6 : Commande par défaut pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

