"""
URLconf for registration using django-registration's simple one-step
workflow.

"""

from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from registration.views import ClientRegistrationView, GarageRegistrationView, processing_login, payment_register, braintree_client_token

urlpatterns = [
    url(r'^processing-login/$', processing_login, name='processing'),
    url(r'^register-client/payment-method/$', payment_register, name='payment_register'),
    url(r'^register-client/payment-method/client_token$', braintree_client_token, name='client_token'),
    url(r'^register-client/$',
        ClientRegistrationView.as_view(),
        name='registration_register_client'),
    url(r'^register-garage/$',
        GarageRegistrationView.as_view(),
        name='registration_register_garage'),
    url(r'', include('registration.auth_urls')),
]
