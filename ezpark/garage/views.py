from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is the garage home page")

def analytics(request):
    return HttpResponse("This is the garage analytics page")

def payment(request):
    return HttpResponse("This is the garage payment page")

def history(request):
    return HttpResponse("This is the garage history page")
