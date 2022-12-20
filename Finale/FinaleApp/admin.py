from django.contrib import admin

# Register your models here.

from FinaleApp.models import Booking, Delivery, Order

admin.site.register(Booking)
admin.site.register(Delivery)
admin.site.register(Order)