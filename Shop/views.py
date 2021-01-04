from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request, 'home.html',{"title":home})

def login(request):
	return render(request, 'login.html',{"title":login})

def register(request):
	return render(request, 'register.html',{"title":register})


def dashboard(request):
	return render(request, 'dashboard.html',{"title":dashboard})


