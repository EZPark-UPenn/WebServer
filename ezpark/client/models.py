from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    braintree_id = models.CharField(max_length=36, null=True)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Car(models.Model):
    client = models.ForeignKey(Client, related_name='cars')
    license_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    parked_in = models.ForeignKey('garage_manager.GarageManager', related_name='cars_in_garage', default=None, null=True)

    def __str__(self):
        return "{} {} with license plate: {}".format(self.make, self.model, self.license_plate)

class Transaction(models.Model):
    car = models.ForeignKey(Car, related_name='history_payments')
    garage = models.ForeignKey('garage.Garage', related_name='history_transactions')
    amount = models.IntegerField(null=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True)
    image_in = models.ImageField(upload_to="in", null=True)
    image_out = models.ImageField(upload_to="out", null=True)

    def __str__(self):
        return "{} parked in {} at {}".format(self.car, self.garage, self.time_in)