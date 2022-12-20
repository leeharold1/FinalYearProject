from django.db import models

class Delivery(models.Model):
    userID = models.CharField(primary_key=True, max_length=50)
    customerName = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    totalCost = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    userID = models.CharField(primary_key=True, max_length=50)
    customerName = models.CharField(max_length=150)
    pickupTime = models.DateTimeField()
    totalCost = models.DecimalField(max_digits=8, decimal_places=2)

class Booking(models.Model):
    userID = models.CharField(primary_key=True, max_length=50)
    customerName = models.CharField(max_length=150)
    time = models.DateTimeField()
    partySize = models.PositiveSmallIntegerField()
