
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from .models import *
from .forms import * 
# Create your views here.

# home view 
def profile(request):
	orders = Order.objects.all()
	client = Client.objects.all()
	total_order = orders.count()
	delivered = orders.filter(status='delivered').count()
	pending = orders.filter(status='pending').count()
	out_delivery = orders.filter(status='out for delivery').count()

	context= {'client': client, 'orders': orders, 
	'total_order': total_order, 'delivered': delivered, 'pending': pending, 
	'out_delivery':out_delivery }
	return render(request, 'user_account/profile.html', context)

# for customer profile 
def customer(request, pk):
	customer = Client.objects.get(id=pk)

	orders= client.order_set_all()
	order_count = orders.count()

	context = {'customer':customer, 'orders': orders, 'order_count':order_count}
	return render(request, 'account/customer.html', context)

# cart page 

def cart(request):
	context= {}
	return render(request, 'store/cart.html', context)

#Checkout 
def checkout(request):
	context= {}
	return render(request, 'store/checkout.html', context)

#Product 
def product(request):
	context= {}
	return render(request, 'store/product.html', context)

# Create Order 
def createOrder(request):
	#OrderFormSet = inlineformset_factory(Client, Order, fields=('product', 'status', 'client'))
	#customer = Customer.objects.get(id=pk)
	#formset = OrderFormSet()
	form = OrderForm()
	if request.method =='POST':
		#print('Printing post:', request.POST)
		form = OrderForm(request.POST) # throwing the post data into the form 
		if form.is_valid(): # performing valid check 
			form.save() # saving the data in the db 
			return redirect('/')
	context= { 'form':form}
	return render(request, 'user_account/order_form.html', context)


# Update customers order-

def updateOrder(request, pk): # passing the primary key into the request views.

	order = Order.objects.get(id=pk) # get the pk from the oder objects in the db from models
	form = OrderForm(instance=order) # pass the instance into the form so it populate the form 

	# sending the data as post data and redirecting back 
	if request.method =='POST':
		#print('Printing post:', request.POST)
		form = OrderForm(request.POST, instance=order) # throwing the post data into the form 
		if form.is_valid(): # performing valid check 
			form.save() # saving the data in the db 
			return redirect('/')

	context= {'form': form}
	return render(request, 'user_account/order_form.html', context)


# Delete Item 
def delete_item(request, pk):
	item = Order.objects.get(id=pk)
	if request.method =='POST':
		#print('Printing post:', request.POST)
			item.delete() # saving the data in the db 
			return redirect('/')


	context= {'item':item}
	return render(request, 'store/delete.html', context)

# Add customer
def addClient(request):
	form = addCustomerForm()
	if request.method == 'POST':
		#print('Printing post:', request.POST)
		form = addCustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context= {'form':form}
	return render(request, 'user_account/add_client.html', context)

# Edit Customer- not yet working
def editClient(request, pk): 
	customer = Client.objects.get(id=pk) 
	form = addCustomerForm(instance=customer) 
	if request.method =='POST':
		form = addCustomerForm(request.POST , instance=customer) 
		if form.is_valid(): # performing valid check 
			form.save() # saving the data in the db 
			return redirect('profile')


	 
	context= {'form': form}
	return render(request, 'user_account/add_client.html', context)