from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username , password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request , 'accounts/login.html',{'error' : 'UserName Or Password Is Incoorect'})

	else:
		return render(request,'accounts/login.html')


def register_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				return render(request , 'accounts/register.html',{'error': 'Username Has Already Been Taken'})
		if password1 != password2:
			return render(request , 'accounts/register.html',{'error': 'Password DoesNot Match'})
		else:
			user = User.objects.create_user(username = username,password = password1)
			auth.login(request,user)
			return redirect('home')
	else:
		return render(request , 'accounts/register.html')


def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('accounts:login')
