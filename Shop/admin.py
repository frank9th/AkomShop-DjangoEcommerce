
from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.
from .models import *


class AppAdmin(AdminSite):
    def index(self, request, extra_context=None):
        # Update extra_context with new variables
        return super().index(request, extra_context)


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(PlacedOrder)


