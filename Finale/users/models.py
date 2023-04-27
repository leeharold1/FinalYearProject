from django.db import models

# Create your models here.


class Reservations(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateField()
	time = models.TimeField()
	party_size = models.IntegerField()

	def __str__(self):
		return self.name