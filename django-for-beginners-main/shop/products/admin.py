
from django.contrib import admin
from .models import Booking, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

# Register your models here.
admin.site.register(Product, ProductAdmin)

class BuyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'amount', 'date', 'feedback')

admin.site.register(Booking, BuyAdmin)

