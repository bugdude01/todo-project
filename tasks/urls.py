from django.urls import path
from . import views

urlpatterns = [
	path('', views.alltasks, name='alltasks'),
	path('home/', views.home, name='home'),
]