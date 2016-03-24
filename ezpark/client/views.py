from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from client.forms import CarRegistrationForm
from client.models import Client, Car, Transaction
from garage.models import Garage

from datetime import datetime, timedelta

def home(request):
    user = User.objects.get(username=request.user)
    client = Client.objects.get(user=user)

    today = datetime.now()
    last_day = today.replace(day=1, hour=0, minute=0, second=0)
    first_day = (last_day - timedelta(days=1)).replace(day=1)

    all_transactions = Transaction.objects.filter(car__in=client.cars.all())
    transactions_last_month = all_transactions.filter(time_in__gte=first_day, time_in__lt=last_day)
    transactions = all_transactions.filter(time_in__gt=today - timedelta(days=7))

    num_garages = len(Garage.objects.filter(history_transactions__in=all_transactions).distinct())
    num_cars = client.cars.count()

    amount = 0
    for transaction in transactions_last_month:
        amount += transaction.amount

    context = {'user': user, 'client': client, 'num_cars': num_cars, 'transactions': transactions, 'num_garages': num_garages, 'amount': amount}
    return render(request, 'client/index.html', context)

def cars(request):
    user = User.objects.get(username=request.user)
    client = Client.objects.get(user=user)
    cars = client.cars.all()
    context = {'user': user, 'client': client, 'cars': cars}
    return render(request, 'client/cars-overview.html', context)

def register_car(request):
    user = User.objects.get(username=request.user)
    client = Client.objects.get(user=user)

    if request.method == 'POST':
        form = CarRegistrationForm(request.POST)
        if form.is_valid():
            car = Car(make=request.POST['make'], model=request.POST['model'],
                  color=request.POST['color'], state=request.POST['state'],
                  license_plate=request.POST['license_plate'], client=client)
            car.save()
            return redirect('/client/cars-overview')
    else:
        form = CarRegistrationForm()

    context = {'user': user, 'client': client, 'form': form}
    return render(request, 'client/register-car.html', context)

def car_history(request):
    user = User.objects.get(username=request.user)
    client = Client.objects.get(user=user)
    context = {'user': user, 'client': client}
    return HttpResponse("Hello, world. You're at the client's car's history.")

def client_history(request):
    user = User.objects.get(username=request.user)
    client = Client.objects.get(user=user)
    all_transactions = Transaction.objects.filter(car__in=client.cars.all())

    context = {'user': user, 'client': client, 'transactions': all_transactions}
    return render(request, 'client/client-history.html', context)
    # return HttpResponse("Hello, world. You're at the client's overall history.")

def client_payment(request):
    return HttpResponse("Hello, world. You're at the client's payment method.")