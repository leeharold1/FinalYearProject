from django.contrib import admin

from .models import Reservations
from .models import DeliveryOrder
from .models import CollectionOrder

# Register your models here.

admin.site.register(Reservations)
admin.site.register(DeliveryOrder)
admin.site.register(CollectionOrder)