from django.db import models

# Create your models here.

class ShopInventory(models.Model):
    part_name = models.CharField(max_length=100)
    part_price = models.DecimalField(max_digits=6, decimal_places=2)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    def __str__(self):
        return self.part_name


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    def __str__(self):
        return self.name