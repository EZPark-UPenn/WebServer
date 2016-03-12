from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^get-user/(?P<license_plate>[\w]+)/$', views.get_user, name='get_user')
]