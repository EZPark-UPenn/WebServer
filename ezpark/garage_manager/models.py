from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GarageManager(models.Model):
    garage = models.OneToOneField('garage.Garage', on_delete=models.CASCADE)

    def __str__(self):
        return "{}'s manager".format(self.garage.user.username)