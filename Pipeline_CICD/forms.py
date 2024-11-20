from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']  # Liste des champs à inclure dans le formulaire

    # Ajouter des validations personnalisées si nécessaire
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Le titre de la tâche ne peut pas être vide.")
        return title