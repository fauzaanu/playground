from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    pizza = models.ManyToManyField(Pizza)

    def __str__(self):
        return self.name
