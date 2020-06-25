from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('alltasks', views.alltasks, name='alltasks'),
	path('completed', views.completed, name='completed'),
	path('add', views.add, name='add'),
	path('<int:task_id/>', views.detail, name='detail'),
]