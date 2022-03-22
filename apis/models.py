from django.db import models

# Create your models here.

class ShopInventory(models.Model):
    part_name = models.CharField(max_length=100)
    part_price = models.CharField(max_length=100)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    def __str__(self):
        return self.part_name
