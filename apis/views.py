from django.shortcuts import render
from rest_framework import viewsets
from .models import ShopInventory,PairMechanic
from .serializers import ShopInventorySerializer,PairMechanicSerializer
# Create your views here.

class ShopInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer



class PairMechanicViewSet(viewsets.ModelViewSet):
    queryset = PairMechanic.objects.all()
    serializer_class = PairMechanicSerializer


