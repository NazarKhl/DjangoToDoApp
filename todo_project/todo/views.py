from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

# Create your views here.

def task_list(reqeust):
    tasks = Task.objects.all()
    return render(reqeust, 'todo/task_list.html', {'tasks': tasks})

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.completed = not task.completed  # Перемикаємо статус
        task.save()  # Зберігаємо зміни
        
    return redirect('task_list')  # Повертаємо на сторінку зі списком завдань

