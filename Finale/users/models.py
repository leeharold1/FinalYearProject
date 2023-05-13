from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reservations(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return self.name

class DeliveryOrder(models.Model):
    deliveryID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
