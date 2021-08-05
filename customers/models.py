from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField()
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
