from django.contrib import admin

from .models import Reservations
from .models import DeliveryOrder

# Register your models here.

admin.site.register(Reservations)
admin.site.register(DeliveryOrder)