from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^cars/register', views.register_car, name='register_car'),
    url(r'^cars/history', views.car_history, name='car_history'),
    url(r'^cars', views.cars, name='cars'),
    url(r'^history', views.client_history, name='client_history'),
    url(r'^payment', views.client_payment, name='client_payment'),
]