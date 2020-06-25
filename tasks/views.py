from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.utils import timezone

def home(request):
	tasks = Task.objects
	return render(request, 'tasks/home.html', {'tasks':tasks})

def alltasks(request):
	tasks = Task.objects
	return render(request, 'tasks/alltasks.html', {'tasks':tasks})#


def completed(request):
	tasks = Task.objects
	return render(request, 'tasks/completed.html', {'tasks':tasks})

@login_required
def add(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['description']:
			task = Task()
			task.title = request.POST['title']
			task.description = request.POST['description']
			task.date_set = timezone.datetime.now()
			task.completed = False
			task.save()
			return redirect('/tasks/' + str(task.id))
		else:
			return render(request, 'tasks/add.html',{'error', 'All fields are required.'})
	else:
		return render(request, 'tasks/add.html')

def detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	return render(request, 'tasks/detail.html',{'task':task})