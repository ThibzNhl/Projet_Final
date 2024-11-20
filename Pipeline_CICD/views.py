from django.shortcuts import render, redirect,get_object_or_404
from .models import Pipeline
from .models import Task
from .forms import TaskForm

def pipeline_list(request):
    pipelines = Pipeline.objects.all()
    return render(request, 'pipeline_list.html', {'pipelines': pipelines})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde la tâche dans la base de données
            return redirect('task_list')  # Redirige vers la liste des tâches
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Met à jour la tâche dans la base de données
            return redirect('task_list')  # Redirige vers la liste des tâches
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')  # Redirige vers la liste des tâches après suppression