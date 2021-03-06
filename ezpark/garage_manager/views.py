import braintree

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from client.models import Car, Transaction

from garage_manager.models import GarageManager

from garage.models import Garage

from datetime import datetime, timedelta

import sys
import pytz

# Create your views here.
def get_client(request, license_plate):
	response = "<p>The license plate was {}.<p>".format(license_plate)
	car = Car.objects.get(license_plate=license_plate)
	response += "<p>The car make and model is {} {}.<p>".format(car.make, car.model)
	client = car.client
	response += "<p>The user is {} {}<p>".format(client.user.first_name, client.user.last_name)
	return HttpResponse(response)

def demo(request):

    latest = Transaction.objects.latest('time_in')

    context = {'transaction': latest }
    return render(request, 'garage-manager/index.html', context)

def enter(car, garage, garage_manager):
	print "Logging Entry..."
	image = None
	start = datetime.now()
	transaction = Transaction(car=car, garage=garage, time_in=start, image_in=image)
	transaction.save()

	# TODO: open gate here

	car.parked_in = garage_manager
	car.save()
	response = "{} {}'s car entered {}.".format(car.client.user.first_name, car.client.user.last_name, garage.user.username)
	return response

def exit(car, garage_manager):
	print "Logging Exit..."
	transaction = Transaction.objects.get(car=car, time_out=None)
	transaction.time_out = datetime.now()

	amt_time = transaction.time_out.replace(tzinfo=None) - transaction.time_in.replace(tzinfo=None)
	# TODO: calculate amount here
	amount = amt_time.seconds * 0.5 
	transaction.amount = amount

	image = None
	transaction.image_out = image
	transaction.save()

	client = car.client
	cid = client.braintree_id

	result = braintree.Transaction.sale({
		"customer_id": cid,
		"amount": str(amount),
		"options": {
			"submit_for_settlement": True
		}
	})

	# TODO: open gate
	car.parked_in = None
	car.save()
	response = "{} {}'s car exited {}.".format(car.client.user.first_name, car.client.user.last_name, garage_manager.garage.user.username)
	return response

@csrf_exempt
@require_http_methods(["POST"])
def log_car(request):
	license_plate = request.POST["license_plate"]
	gid = request.POST["gid"]
	garage = Garage.objects.get(id=gid)
	garage_manager = GarageManager.objects.get(garage=garage)
	car = Car.objects.get(license_plate=license_plate)

	if car in garage_manager.cars_in_garage.all():
		response = exit(car, garage_manager)
		return HttpResponse(response)
	response = enter(car, garage, garage_manager)
	return HttpResponse(response)

def local_log_car(alpr_data, gid):
	sys.stdout = open("/home/ubuntu/logs.txt", "a")
	print "ENTERED CAR LOG.............."

	print "GID: ", gid

	garage = Garage.objects.get(id=gid)
	garage_manager = GarageManager.objects.get(garage=garage)

	car = None
	license_plate = None

	candidates = alpr_data[0]["candidates"]
	for candidate in candidates:
		license_plate = candidate["plate"]
		if Car.objects.filter(license_plate=license_plate).exists():
			car = Car.objects.get(license_plate=license_plate)
			break

	response = {}
	if not car:
		response["open_gate"] = False
		response["plate_detected"] = alpr_data[0]["plate"]
	else:
		if is_recent(license_plate):
			response["open_gate"] = False
			response["plate_detected"] = license_plate
			response["message"] = "Recently detected this license plate"
		else:
			if car in garage_manager.cars_in_garage.all():
				exit(car, garage_manager)
			else:
				enter(car, garage, garage_manager)

			response["open_gate"] = True
			response["plate_detected"] = license_plate
			response["message"] = "Opening gate"
	print response
	sys.stdout.flush()
	return response

def is_recent(license_plate):
	transactions = []
	transactions.append(Transaction.objects.latest('time_in'))
	transactions.append(Transaction.objects.latest('time_out'))
	now = datetime.now(pytz.utc)
	diff = timedelta(seconds=20)

	for transaction in transactions:
		#if transaction.car.license_plate == license_plate:

		din = now - transaction.time_in
		print "Din: " , din
		if (din < diff):
			return True
		if transaction.time_out != None:
			dout = now - transaction.time_out
			print "Dout: " , dout
			if (dout < diff):
				return True
	return False

