from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('shopinventory', views.ShopInventoryViewSet)
router.register('pairmechanic', views.PairMechanicViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
]
