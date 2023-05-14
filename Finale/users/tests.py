from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Reservations, DeliveryOrder

# Create your tests here.

class ReservationsModelTestCase(TestCase):
    def setUp(self):
        # Create a sample reservation for testing
        self.reservation = Reservations.objects.create(
            name='John Doe',
            date=timezone.now().date(),
            time=timezone.now().time(),
            party_size=4
        )

    def test_reservation_str(self):
        # Test the __str__ method of the Reservations model
        # It should return the name of the reservation
        self.assertEqual(str(self.reservation), 'John Doe')

class DeliveryOrderModelTestCase(TestCase):
    def setUp(self):
        # Create a sample user and delivery order for testing
        self.user = User.objects.create(username='testuser')
        self.delivery_order = DeliveryOrder.objects.create(
            customer=self.user,
            address='123 Main St',
            order='Coke(330ml) ,Margherita(Small) ,Chicken Tenders(Medium)',
            price=13.80,
            notes='Extra cheese'
        )

    def test_delivery_order_primary_key(self):
        # Test if the primary key (deliveryID) of the delivery order is not None
        self.assertIsNotNone(self.delivery_order.deliveryID)

    def test_delivery_order_customer(self):
        # Test if the customer of the delivery order is the same as the created user
        self.assertEqual(self.delivery_order.customer, self.user)

    def test_delivery_order_order(self):
        # Test if the order of the delivery order is set correctly
        self.assertEqual(self.delivery_order.order, 'Coke(330ml) ,Margherita(Small) ,Chicken Tenders(Medium)')

    def test_delivery_order_price(self):
        # Test if the price of the delivery order is set correctly
        self.assertEqual(self.delivery_order.price, 13.80)