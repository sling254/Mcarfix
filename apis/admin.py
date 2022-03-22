from django.contrib import admin
from .models import ShopInventory,Mechanic,ServiceOffered,PairMechanic
# Register your models here.


admin.site.register(ShopInventory)
admin.site.register(Mechanic)
admin.site.register(ServiceOffered)
admin.site.register(PairMechanic)