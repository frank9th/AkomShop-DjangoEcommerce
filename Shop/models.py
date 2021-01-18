from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name 


class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField()
	food = models.BooleanField(default=False, null=True, blank=False)
	digital = models.BooleanField(default=False, null=True, blank=False)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name + "|"+ str(self.digital)


	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	

class Order(models.Model):
	STATUS =(
		('Delivered', 'Delivered'),
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'), 
		)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=False)
	transaction_id = models.CharField(max_length=200, null=True)
	status = models.BooleanField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return str(self.complete) + " | " + str(self.id) 

	# logic to display shipping form if physical product is in cart
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True

		return shipping
	
	# total price of items in cart 
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	# total quantity of itmes in cart 
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total



class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name + " | " + str(self.date_added)


#fuction for calculating the totoal of product - this is a propert of orderItems
	@property
	def get_total(self):
		total = self.product.price * self.quantity

		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	landmark = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	zipcode = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return self.address + " |  " + self.customer.name + " | " + self.order.transaction_id


class PlacedOrder(models.Model):
	STATUS =(

		('Delivered', 'Delivered'),
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'), 
		)
		
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	product = models.ManyToManyField(Product)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	address = models.CharField(max_length=200, null=True)
	total = models.FloatField()
	status = models.BooleanField(max_length=200, null=True, choices=STATUS, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customer
