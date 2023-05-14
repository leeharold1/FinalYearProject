from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Reservations

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