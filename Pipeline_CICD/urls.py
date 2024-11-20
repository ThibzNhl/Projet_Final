from django.urls import path
from Pipeline_CICD import views

urlpatterns = [
    path('', views.pipeline_list, name='pipeline_list'),  # Page d'accueil pour cette application
    path('tasks/', views.task_list, name='task_list'),  # Liste des tâches
    path('tasks/add/', views.add_task, name='add_task'),  # Vue pour ajouter une tâche
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),  # Vue pour modifier une tâche
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Route pour supprimer une tâche
]
