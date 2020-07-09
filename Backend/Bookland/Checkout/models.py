from django.db import models
from django.contrib.auth.models import User
from Books.models import Product


class OrderBook(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    # book = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through='Order')

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(OrderBook, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now=True, null=True)
    company = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} ordered ({self.quantity}) {self.book.title} on {self.ordered_date}'
