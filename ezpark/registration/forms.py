"""
Forms and validation code for user registration.

Note that all of these forms assume your user model is similar in
structure to Django's default User class. If your user model is
significantly different, you may need to write your own form class;
see the documentation for notes on custom user models with
django-registration.

"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from . import validators


User = get_user_model()


class ClientRegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.

    """
    # Explicitly declared here because Django's default
    # UserCreationForm, which we subclass, does not require this field
    # but workflows in django-registration which involve explicit
    # activation step do require it. If you need an optional email
    # field, simply subclass and declare the field not required.
    email = forms.EmailField(
        help_text=_(u'email address'),
        required=True
    )

    license_plate = forms.CharField(max_length=20)
    make = forms.CharField(max_length=20)
    model = forms.CharField(max_length=30)
    color = forms.CharField(max_length=10)
    state = forms.CharField(max_length=2)

    class Meta(UserCreationForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'

    def clean(self):
        """
        Apply the reserved-name validator to the username.

        """
        # This is done in clean() because Django does not currently
        # have a non-ugly way to just add a validator to an existing
        # field on a form when subclassing; the standard approach is
        # to re-declare the entire field in order to specify the
        # validator. That's not an option here because we're dealing
        # with the user model and we don't know -- given custom users
        # -- how to declare the username field.
        #
        # So defining clean() and attaching the error message (if
        # there is one) to the username field is the least-ugly
        # solution.
        username_value = self.cleaned_data.get(User.USERNAME_FIELD)
        if username_value is not None:
            try:
                if hasattr(self, 'reserved_names'):
                    reserved_names = self.reserved_names
                else:
                    reserved_names = validators.DEFAULT_RESERVED_NAMES
                validator = validators.ReservedNameValidator(
                    reserved_names=reserved_names
                )
                validator(username_value)
            except ValidationError as v:
                self.add_error(User.USERNAME_FIELD, v)


class GarageRegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.

    """
    # Explicitly declared here because Django's default
    # UserCreationForm, which we subclass, does not require this field
    # but workflows in django-registration which involve explicit
    # activation step do require it. If you need an optional email
    # field, simply subclass and declare the field not required.
    email = forms.EmailField(
        help_text=_(u'email address'),
        required=True
    )

    address = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=11)

    class Meta(UserCreationForm.Meta):
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        required_css_class = 'required'

    def clean(self):
        """
        Apply the reserved-name validator to the username.

        """
        # This is done in clean() because Django does not currently
        # have a non-ugly way to just add a validator to an existing
        # field on a form when subclassing; the standard approach is
        # to re-declare the entire field in order to specify the
        # validator. That's not an option here because we're dealing
        # with the user model and we don't know -- given custom users
        # -- how to declare the username field.
        #
        # So defining clean() and attaching the error message (if
        # there is one) to the username field is the least-ugly
        # solution.
        username_value = self.cleaned_data.get(User.USERNAME_FIELD)
        if username_value is not None:
            try:
                if hasattr(self, 'reserved_names'):
                    reserved_names = self.reserved_names
                else:
                    reserved_names = validators.DEFAULT_RESERVED_NAMES
                validator = validators.ReservedNameValidator(
                    reserved_names=reserved_names
                )
                validator(username_value)
            except ValidationError as v:
                self.add_error(User.USERNAME_FIELD, v)


# class RegistrationFormTermsOfService(RegistrationForm):
#     """
#     Subclass of ``RegistrationForm`` which adds a required checkbox
#     for agreeing to a site's Terms of Service.

#     """
#     tos = forms.BooleanField(
#         widget=forms.CheckboxInput,
#         label=_(u'I have read and agree to the Terms of Service'),
#         error_messages={
#             'required': validators.TOS_REQUIRED,
#         }
#     )


# class RegistrationFormUniqueEmail(RegistrationForm):
#     """
#     Subclass of ``RegistrationForm`` which enforces uniqueness of
#     email addresses.

#     """
#     def clean_email(self):
#         """
#         Validate that the supplied email address is unique for the
#         site.

#         """
#         if User.objects.filter(email__iexact=self.cleaned_data['email']):
#             raise forms.ValidationError(validators.DUPLICATE_EMAIL)
#         return self.cleaned_data['email']
