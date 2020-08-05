from django.contrib import admin
from .models import CustomerLocation, CustomerOrder


class CustomerLocationClass(admin.ModelAdmin):
    list_display = ('customer', 'street_address', 'city', 'country')


admin.site.register(CustomerLocation, CustomerLocationClass)


class CustomerOrderClass(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'price', 'ordered_date')


admin.site.register(CustomerOrder, CustomerOrderClass)
