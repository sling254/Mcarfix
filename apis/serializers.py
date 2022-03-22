from rest_framework import serializers
from .models import ShopInventory, PairMechanic


class ShopInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopInventory
        fields = ('part_name', 'part_price', 'car_make', 'car_model')


class PairMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairMechanic
        fields = ('mechanic', 'service')