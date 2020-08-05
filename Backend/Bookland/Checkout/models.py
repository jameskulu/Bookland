from django.db import models
from django.contrib.auth.models import User
from Books.models import Product


class CustomerLocation(models.Model):
    company = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.username}'s location"


class CustomerOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        CustomerLocation, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.customer.username} ordered ({self.quantity}) {self.product} on {self.ordered_date}"
