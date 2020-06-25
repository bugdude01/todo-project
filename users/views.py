from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == 'POST':
		#user wants to sign up
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'users/signup.html', {'error': 'Sorry, username has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request, 'users/signup.html', {'error': 'Passwords must match'})

	else:
		#user wants to enter info
		return render(request, 'users/signup.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'users/login.html', {'error': 'username or password is invalid'})
	return render(request, 'users/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')	