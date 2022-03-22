from django.db import models

# Create your models here.

class ShopInventory(models.Model):
    part_name = models.CharField(max_length=100)
    part_price = models.DecimalField(max_digits=6, decimal_places=2)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    def __str__(self):
        return {'part_name': self.part_name}

class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceOffered(models.Model):
    service_Offered = models.CharField(max_length=100)
    def __str__(self):
        return self.service_Offered


class PairMechanic(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceOffered, on_delete=models.CASCADE)
    def __str__(self):
        return self.mechanic.name + " offers " + self.service.service_Offered