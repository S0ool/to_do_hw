from django.shortcuts import render
from .models import Task


# Create your views here.

def index(request):
    tasks = Task.objects.values_list('id', 'title')
    print(tasks)
    return render(request, 'app/index.html', {'tasks': tasks})
def task_filter(request):
    tasks = Task.objects.filter(title__contains='title').values_list('title')
    print(tasks)
    return render(request, 'app/index.html', {'tasks': tasks})
