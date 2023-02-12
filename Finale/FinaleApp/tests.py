from django.test import TestCase
from .models import *
import pytz

timezone = pytz.timezone("Europe/Dublin")
# Create your tests here.

class DeliveryTest(TestCase):
    def test_model_can_create_a_table(self):
        # create an instance of the model
        instance = Delivery.objects.create(
            userID = '1234'
            , customerName = 'Lee'
            , address = 'address'
            , totalCost = 12.50
        )

        # check if the instance was created successfully
        self.assertIsNotNone(instance)

        # check if the instance has the expected values
        self.assertEqual(instance.userID, '1234')
        self.assertEqual(instance.customerName, 'Lee')
        self.assertEqual(instance.address, 'address')
        self.assertEqual(instance.totalCost, 12.50)

#--------------------------------------------------------------------------------------

class OrderTest(TestCase):
    def test_model_can_create_a_table(self):
        # create an instance of the model
        instance = Order.objects.create(
            userID = '4321'
            , customerName = 'Bob'
            , pickupTime = '2023-2-12 15:00:00 +0000'
            , totalCost = 30.00
        ) 

        # check if the instance was created successfully
        self.assertIsNotNone(instance)

        # check if the instance has the expected values
        self.assertEqual(instance.userID, '4321')
        self.assertEqual(instance.customerName, 'Bob')
        self.assertEqual(instance.pickupTime, '2023-2-12 15:00:00 +0000' ) 
        self.assertEqual(instance.totalCost, 30.00)

#--------------------------------------------------------------------------------------

class BookingTest(TestCase):
    def test_model_can_create_a_table(self):
        # create an instance of the model
        instance = Booking.objects.create(
            userID = '0000'
            , customerName = 'Mary'
            , time = '2023-2-14 19:30:00 +0000'
            , partySize = 2
        ) 

        # check if the instance was created successfully
        self.assertIsNotNone(instance)

        # check if the instance has the expected values
        self.assertEqual(instance.userID, '0000')
        self.assertEqual(instance.customerName, 'Mary')
        self.assertEqual(instance.time, '2023-2-14 19:30:00 +0000' ) 
        self.assertEqual(instance.partySize, 2)