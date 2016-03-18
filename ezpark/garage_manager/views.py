from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from client.models import Car, Transaction

from garage_manager.models import GarageManager

from garage.models import Garage

from datetime import datetime

# Create your views here.
def get_client(request, license_plate):
	response = "<p>The license plate was {}.<p>".format(license_plate)
	car = Car.objects.get(license_plate=license_plate)
	response += "<p>The car make and model is {} {}.<p>".format(car.make, car.model)
	client = car.client
	response += "<p>The user is {} {}<p>".format(client.user.first_name, client.user.last_name)
	return HttpResponse(response)

def enter(request, car, garage, garage_manager):
	image = None
	start = datetime.now()
	transaction = Transaction(car=car, garage=garage, time_in=start, image_in=image)
	transaction.save()

	# TODO: open gate here

	car.parked_in = garage_manager
	car.save()
	response = "{} {}'s car entered {}.".format(car.client.user.first_name, car.client.user.last_name, garage.user.username)
	return HttpResponse(response)

def exit(request, car, garage_manager):
	transaction = Transaction.objects.get(car=car, time_out=None)
	transaction.time_out = datetime.now()

	amt_time = transaction.time_out.replace(tzinfo=None) - transaction.time_in.replace(tzinfo=None)
	# TODO: calculate amount here
	amount = 0
	transaction.amount = amount

	image = None
	transaction.image_out = image
	transaction.save()

	client = car.client
	# TODO: payments stuff here

	# TODO: open gate
	car.parked_in = None
	car.save()
	response = "{} {}'s car exited {}.".format(car.client.user.first_name, car.client.user.last_name, garage_manager.garage.user.username)
	return HttpResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def log_car(request):
	license_plate = request.POST["license_plate"]
	gid = request.POST["gid"]
	garage = Garage.objects.get(id=gid)
	garage_manager = GarageManager.objects.get(garage=garage)
	car = Car.objects.get(license_plate=license_plate)

	if car in garage_manager.cars_in_garage.all():
		return exit(request, car, garage_manager)
	return enter(request, car, garage, garage_manager)