from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GarageManager(models.Model):
	garage = models.OneToOneField('garage.Garage', on_delete=models.CASCADE)