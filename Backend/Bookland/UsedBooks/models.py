from django.db import models
from django.contrib.auth.models import User


class UsedCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        default='image_not_found.png', upload_to='used_books_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categories for Used Book"


class UsedSubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(UsedCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Categories for Used Book"


class UsedProduct(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='used_books',
                              default='image_not_found.png')
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    subcategory = models.ForeignKey(UsedSubCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Used Book"


class UsedComment(models.Model):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(UsedProduct, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.product.title}"

    class Meta:
        verbose_name = "Used Books Comment"
