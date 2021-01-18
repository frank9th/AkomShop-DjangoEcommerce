
from django.db import models

# Create your models here.
class Client(models.Model):
	SEX= (
		('male', 'Male'),
		('female', 'Female'),
		('prefered not to say', 'Prefered not to say')

		)
	full_name = models.CharField(max_length=200, null=True )
	email = models.CharField(max_length=200, null=True )
	phone = models.CharField(max_length=200, null=True )
	address = models.CharField(max_length=200, null=True )
	sex = models.CharField(max_length=200, null=True, choices=SEX)
	date_created = models.DateTimeField(auto_now_add= True, null=True )

	def __str__(self):
		return self.full_name

class Vendor(models.Model):
	SEX= (
		('male', 'Male'),
		('female', 'Female')
		)
	CATHEGORY= (
		('goods', 'Goods/Product'),
		('service', 'Services'),
		('fast food ', 'Fast Food')

		)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True )
	phone = models.CharField(max_length=200, null=True )
	address = models.CharField(max_length=200, null=True )
	sex = models.CharField(max_length=200, null=True, choices=SEX)
	business_name = models.CharField(max_length=200, null=True )
	business_type = models.CharField(max_length=200, null=True, choices=CATHEGORY)
	date_created = models.DateTimeField(auto_now_add= True, null=True )

	def __str__(self):
		return self.first_name

# This counld be option- its said to be the link btwn product and order 
class Tag(models.Model):
	name = models.CharField(max_length=200, null=True )

	def __str__(self):
		return self.name 


class Product(models.Model):
	CATHEGORY= (
		('Food', 'Food'),
		('Food Item', 'Food Item')

		)
	name = models.CharField(max_length=200, null=True )
	price = models.FloatField( null=True )
	cathegory = models.CharField(max_length=200, null=True, choices=CATHEGORY)
	description = models.CharField(max_length=200, null=True )
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name 


class Service(models.Model):
	name = models.CharField(max_length=200, null=True )
	price = models.FloatField( null=True )
	duration = models.CharField(max_length=200, null=True )


	def __str__(self):
		return self.name 

class Order(models.Model):
	ORDER_STATE= (
		('pending', 'Pending'),
		('delivered', 'Delivered'),
		('out for delivery', 'out for delivery'),
		('cancled', 'Cancled')

		)

	client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
	item_name = models.CharField(max_length=200, null=True )
	price = models.FloatField( null=True)
	vendor = models.ForeignKey(Vendor, null=True, blank=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add= True, null=True )
	status = models.CharField(max_length=200, null=True, choices=ORDER_STATE)
	dprice = models.FloatField( max_length=200, null=True, blank=True)

	"""docstring for Order"""
	def __str__(self):
		return self.item_name