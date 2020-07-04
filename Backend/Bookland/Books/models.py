from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        default='image_not_found.png', upload_to='categories')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products',
                              default='no_image_found.png')
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    out_of_stock = models.BooleanField(default=False, null=True, blank=True)
    favrioute = models.ManyToManyField(
        User, related_name='favrioute', blank=True)

    def __str__(self):
        return self.title
