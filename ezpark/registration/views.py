"""
Base view classes for all registration workflows.

"""

from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, get_user_model, login
from django.http import HttpResponse

from registration import signals
from registration.forms import ClientRegistrationForm, GarageRegistrationForm

from client.models import Client, Car
from garage.models import Garage

import braintree

User = get_user_model()
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="fkchrkdh3t7nh2kd",
                                  public_key="bspwxc85cxjh6dpx",
                                  private_key="0ad5811c83fcc2b5adc7189bb06b9b33")


def processing_login(request):
    url = '/register-client/'
    user = User.objects.get(username=request.user)
    if Client.objects.filter(user=user).exists():
        return redirect('/client/home')
    if Garage.objects.filter(user=user).exists():
        return redirect('/garage/home')
    return redirect(url)

def payment_register(request):
    if request.method == "POST":
        nonce = request.POST["payment_method_nonce"]
        user = User.objects.get(username=request.user)

        result = braintree.Customer.create({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "payment_method_nonce": nonce
        })
        
        if result.is_success:
            print result.customer.id # TODO: Add this customer ID to client model
            return redirect('/client/home')
        else:
            return HttpResponse("Failure")

    elif request.method == "GET":
        return render(request, 'registration/payment_registration_form.html')

def braintree_client_token(request):
    return HttpResponse(braintree.ClientToken.generate())


class ClientRegistrationView(FormView):
    """
    Base class for user registration views.

    """
    disallowed_url = 'registration_disallowed'
    form_class = ClientRegistrationForm
    success_url = None
    template_name = 'registration/client_registration_form.html'

    def dispatch(self, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.

        """
        if not self.registration_allowed():
            return redirect(self.disallowed_url)
        return super(ClientRegistrationView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        new_user = self.register(form)
        success_url = self.get_success_url(new_user)

        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def form_invalid(self, form):
        # tl;dr -- this method is implemented to work around Django
        # ticket #25548, which is present in the Django 1.9 release
        # (but not in Django 1.8).
        #
        # The longer explanation is that in Django 1.9,
        # FormMixin.form_invalid() does not pass the form instance to
        # get_context_data(). This causes get_context_data() to
        # construct a new form instance with the same data in order to
        # put it into the template context, and then any access to
        # that form's ``errors`` or ``cleaned_data`` runs that form
        # instance's validation. The end result is that validation
        # gets run twice on an invalid form submission, which is
        # undesirable for performance reasons.
        #
        # Manually implementing this method, and passing the form
        # instance to get_context_data(), solves this issue (which was
        # fixed in Django 1.9.1 and will not be present in Django
        # 1.10).
        return self.render_to_response(self.get_context_data(form=form))

    def registration_allowed(self):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.

        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        client = Client(user=new_user)
        client.save()
        data = self.request.POST
        car = Car(make=data['make'], model=data['model'],
                  color=data['color'], state=data['state'],
                  license_plate=data['license_plate'], client=client)
        car.save()
        return new_user

    def get_success_url(self, user):
        return '/register-client/payment-method/'


class GarageRegistrationView(FormView):
    """
    Base class for user registration views.

    """
    disallowed_url = 'registration_disallowed'
    form_class = GarageRegistrationForm
    success_url = None
    template_name = 'registration/garage_registration_form.html'

    def dispatch(self, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.

        """
        if not self.registration_allowed():
            return redirect(self.disallowed_url)
        return super(GarageRegistrationView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        new_user = self.register(form)
        success_url = self.get_success_url(new_user)

        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def form_invalid(self, form):
        # tl;dr -- this method is implemented to work around Django
        # ticket #25548, which is present in the Django 1.9 release
        # (but not in Django 1.8).
        #
        # The longer explanation is that in Django 1.9,
        # FormMixin.form_invalid() does not pass the form instance to
        # get_context_data(). This causes get_context_data() to
        # construct a new form instance with the same data in order to
        # put it into the template context, and then any access to
        # that form's ``errors`` or ``cleaned_data`` runs that form
        # instance's validation. The end result is that validation
        # gets run twice on an invalid form submission, which is
        # undesirable for performance reasons.
        #
        # Manually implementing this method, and passing the form
        # instance to get_context_data(), solves this issue (which was
        # fixed in Django 1.9.1 and will not be present in Django
        # 1.10).
        return self.render_to_response(self.get_context_data(form=form))

    def registration_allowed(self):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.

        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        data = self.request.POST
        garage = Garage(user=new_user, address=data['address'],
                        phone_number=data['phone_number'])
        garage.save()
        return new_user

    def get_success_url(self, user):
        return '/garage/home'
