from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email
