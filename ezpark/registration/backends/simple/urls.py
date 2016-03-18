"""
URLconf for registration using django-registration's simple one-step
workflow.

"""

from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from registration.views import ClientRegistrationView, GarageRegistrationView

urlpatterns = [
    url(r'^register-client/$',
        ClientRegistrationView.as_view(),
        name='registration_register_client'),
    url(r'^register-garage/$',
        GarageRegistrationView.as_view(),
        name='registration_register_garage'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'
        ),
        name='registration_disallowed'),
    url(r'', include('registration.auth_urls')),
]
