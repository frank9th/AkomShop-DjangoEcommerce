from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Order)
