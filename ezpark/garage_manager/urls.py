from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^get-client/(?P<license_plate>[\w]+)/$', views.get_client, name='get_client'),
	url(r'^log-car/$', views.log_car, name='log_car'),
	url(r'^demo', views.demo, name='demo')
]