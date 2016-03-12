from django.shortcuts import render
from django.http import HttpResponse
from client.models import Car

# Create your views here.
def get_user(request, license_plate):
	response = "<p>The license plate was {}.<p>".format(license_plate)
	car = Car.objects.get(license_plate=license_plate)
	response += "<p>The car make and model is {} {}.<p>".format(car.make, car.model)
	client = car.client
	response += "<p>The user is {} {}<p>".format(client.user.first_name, client.user.last_name)
	return HttpResponse(response)