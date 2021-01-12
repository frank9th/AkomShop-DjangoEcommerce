from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only  
from .models import *
from django.http import JsonResponse 
import json 
import datetime
# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages

def home(request):
	return render(request, 'home.html',{"title":home})


def store(request):
	products = Product.objects.all()
	context = {'products':products}

	return render(request, 'store/store.html',  context)
	#return render(request, 'home-page.html',  context)


def home_page(request):
	products = Product.objects.all()
	context = {'products':products}

	#return render(request, 'store/store.html',  context)
	return render(request, 'home-page.html',  context)





def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order ={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

	context = {'items':items, 'order':order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order ={'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

	context = {'items':items, 'order':order}
	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:',  action)
	print('ProductId:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()


	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	#print('Data:', request.body)
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
		if total == order.get_cart_total:
			order.complete = True 
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
				customer=customer,
				order=order, 
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'], 
				)


		# remain to send the shippinh=g info 
	else:
		print('user is not logged in...')

	return JsonResponse('Payment complete', safe=False)



@unauthenticated_user
def loginPage(request):
	
	if request.method == 'POST':
		# assigning varables to the username and password field 
		username = request.POST.get('username')
		password = request.POST.get('password')

		#authenticating the fields through django authentication package 

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('user-dashboard')
		else:
			messages.info(request, 'Username or password is incorrect')

	context = {'messages':messages}
	return render(request, 'login.html', context)

@unauthenticated_user
def register(request):
	
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			
			messages.success(request, 'Account was created for' + username)
			return redirect('login')

	context = {'form':form}
	return render(request, 'register.html', context)

#User Dasbard View 
@login_required(login_url ='login')
#@admin_only
def user_dashboard(request):
	return render(request, 'user_account/user_dashboard.html',{"title":user_dashboard})

# AdminDashbod View 
@login_required(login_url ='login')
@admin_only
@allowed_users('admin')
def admin_dashboard(request):
	context = {}
	return render(request, 'admin_account/admin_dashboard.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')