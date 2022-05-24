from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()