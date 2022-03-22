from rest_framework import serializers
from .models import Mechanic, ShopInventory, PairMechanic


class ShopInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopInventory
        fields = ('part_name', 'part_price', 'car_make', 'car_model')


class PairMechanicSerializer(serializers.ModelSerializer):
    mechanic_name = serializers.CharField(source='mechanic.name')
    service = serializers.CharField(source='service.service_Offered')
    class Meta:
        model = PairMechanic
        fields = ('mechanic_name', 'service')
    

class AddMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairMechanic
        fields = ('mechanic', 'service')