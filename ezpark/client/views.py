from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the client home.")

def cars(request):
    return HttpResponse("Hello, world. You're at the client's cars.")

def register_car(request):
    return HttpResponse("Hello, world. You're at the client's register_car page.")

def car_history(request):
    return HttpResponse("Hello, world. You're at the client's car's history.")

def client_history(request):
    return HttpResponse("Hello, world. You're at the client's overall history.")

def client_payment(request):
    return HttpResponse("Hello, world. You're at the client's payment method.")