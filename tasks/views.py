from django.shortcuts import render

from .models import Task

def home(request):
	tasks = Task.objects
	return render(request, 'tasks/home.html', {'tasks':tasks})


def alltasks(request):
	tasks = Task.objects
	return render(request, 'tasks/alltasks.html', {'tasks':tasks})