from django.contrib import admin 

# Register your models here.

from .models import Product, Customer, Order, OrderItem, ShippingAddress  

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

