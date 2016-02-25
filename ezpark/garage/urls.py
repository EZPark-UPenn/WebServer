from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^home', views.home),
    url(r'^analytics', views.analytics),
    url(r'^payment', views.payment),
    url(r'^history', views.history),
]