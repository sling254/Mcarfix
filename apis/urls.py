from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shopinventory', views.ShopInventoryViewSet)
router.register('pairmechanic', views.AddMechanic) 

urlpatterns = [
    path('', views.apiOverview, name='index'),
    path('shopinventory-list',views.ShopInventoryList, name='ShopInventoryList'),
    path('view-mechanics',views.PairMechanicList, name='PairMechanicList'),
    path('add-items', include(router.urls)),
    
   
]
