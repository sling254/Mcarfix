from django.shortcuts import render
from rest_framework import viewsets
from .models import ShopInventory
from .serializers import ShopInventorySerializer
# Create your views here.

class ShopInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer


