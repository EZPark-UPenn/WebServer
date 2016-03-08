from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Car(models.Model):
	client = models.ForeignKey(Client, related_name='cars')
	license_plate = models.CharField(max_length=20)
	make = models.CharField(max_length=20)
	model = models.CharField(max_length=30)
	color = models.CharField(max_length=10)
	state = models.CharField(max_length=2)

class Transaction(models.Model):
	car = models.ForeignKey(Car, related_name='history_payments')
	garage = models.ForeignKey('garage.Garage', related_name='history_transactions')
	amount = models.IntegerField()
	time_in = models.DateTimeField()
	time_out = models.DateTimeField()
	image_in = models.ImageField(upload_to="in")
	image_out = models.ImageField(upload_to="out")