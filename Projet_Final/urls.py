from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pipeline_CICD.urls')),  # Inclus toutes les URLs de l'application Pipeline_CICD
]
