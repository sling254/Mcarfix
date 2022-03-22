from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import ShopInventory,PairMechanic
from .serializers import ShopInventorySerializer,PairMechanicSerializer
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List':'/shopinventory-list/',
        'Mechanic List':'/view-mechanics/',
        'Add items':'/add-items/',
    }
    return Response(api_urls)
@api_view(['GET'])
def ShopInventoryList(request):
    """
    List all my Spare part Shop inventory.
    """
    if request.method == 'GET':
        ShopItems = ShopInventory.objects.all()
        serializer = ShopInventorySerializer(ShopItems, many=True)
        return JsonResponse({'ShopInventoryList': serializer.data}, safe=False)
                        
@api_view(['GET'])
def PairMechanicList(request):
    """
    List of mechanics and service offred
    """

    if request.method == 'GET':
        Mechanic = PairMechanic.objects.all()
        serializer = PairMechanicSerializer(Mechanic, many=True)
        return JsonResponse({'MechanicList': serializer.data}, safe=False)

class ViewShopInventory(viewsets.ReadOnlyModelViewSet):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer
class ShopInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer



class PairMechanicViewSet(viewsets.ModelViewSet):
    queryset = PairMechanic.objects.all()
    serializer_class = PairMechanicSerializer

class AddMechanic(viewsets.ModelViewSet):
    queryset = PairMechanic.objects.all()
    serializer_class = PairMechanicSerializer


