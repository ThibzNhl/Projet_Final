L'automatisation du cycle de vie logiciel avec les pipelines CI/CD

Application de gestion de tâches (To-Do List)  
Description : Une application web simple où les utilisateurs peuvent ajouter, supprimer, et marquer des tâches comme complétées.  
Technologies : Django pour le backend, HTML/CSS et JavaScript pour le frontend.  
Pipeline CI/CD : Chaque fois qu'une nouvelle fonctionnalité est ajoutée (comme une nouvelle vue pour les tâches), le pipeline s'assure que l'application passe les tests unitaires et fonctionnels (ex: vérifier que l'ajout et la suppression de tâches fonctionnent).  
  
**Étapes du pipeline :**  
Test unitaire : Test des opérations CRUD (Create, Read, Update, Delete) sur les tâches.  
Build Docker : Création d'une image Docker pour l'application Flask.  
Déploiement automatique : Déploiement de l'application sur un serveur distant après validation des tests.  


urls importantes :   
http://localhost:8000/tasks/  
http://localhost:8000/  
http://localhost:8000/admin/  

id: admin   
mot de passe: admin  


créer l'image Docker en local avec la commande :  
docker build -t my-django-app .  

pour tester l’application en local avec Docker:   
docker run -p 8000:8000 my-django-app  

