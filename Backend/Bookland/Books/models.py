from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        default='image_not_found.png', upload_to='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Categorie"


class Product(models.Model):
    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products',
                              default='image_not_found.png')
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    out_of_stock = models.BooleanField(default=False, null=True, blank=True)
    favrioute = models.ManyToManyField(
        User, related_name='favrioute', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"


class Comment(models.Model):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.product.title}"
