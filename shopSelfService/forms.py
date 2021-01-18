from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class addCustomerForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'