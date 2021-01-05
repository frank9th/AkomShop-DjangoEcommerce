from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages

def home(request):
	return render(request, 'home.html',{"title":home})

def loginPage(request):

	if request.method == 'POST':
		# assigning varables to the username and password field 
		username = request.POST.get('username')
		password = request.POST.get('password')

		#authenticating the fields through django authentication package 

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.info(request, 'Username or password is incorrect')




	context = {}
	return render(request, 'login.html', context)

def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account was created')
			return redirect('login')

	context = {'form':form}
	return render(request, 'register.html', context)

@login_required(login_url ='login')
def dashboard(request):
	return render(request, 'dashboard.html',{"title":dashboard})

def logoutUser(request):
	logout(request)
	return redirect('login')