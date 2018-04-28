# Forms that exist to create an account

from carRepo import constants as main_const

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from . import models as acc_models, constants as acc_const


class UserForm(forms.ModelForm):
    """A default form for the built in User Model"""
    class Meta:
        """Form attributes"""
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': acc_const.EMAIL_PLACEHOLDER}),
            'password': forms.HiddenInput(),
        }

    def clean(self):
        """Ensure User data meets certain criteria"""
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError(acc_const.UNIQUE_USERNAME, acc_const.UNIQUE_USERNAME_CODE)
        elif User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(acc_const.UNIQUE_EMAIL, code=acc_const.UNIQUE_EMAIL_CODE)


class EditUserForm(forms.ModelForm):
    """A form to edit user information"""
    class Meta:
        """Form attributes"""
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': acc_const.EMAIL_PLACEHOLDER}),
        }

    def __init__(self, user, *args, **kwargs):
        """Initialize EditUserForm"""
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        """Ensure User data is unique"""
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            username = User.objects.get(username=self.cleaned_data['username']).username
            if username != self.user.username:
                raise ValidationError(acc_const.UNIQUE_USERNAME, acc_const.UNIQUE_USERNAME_CODE)
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            email = User.objects.get(email=self.cleaned_data['email']).email
            if email != self.user.email:
                raise ValidationError(acc_const.UNIQUE_EMAIL, code=acc_const.UNIQUE_EMAIL_CODE)


class ProfileForm(forms.ModelForm):
    """A form to enter more user information through the Profile model"""
    class Meta:
        """Profile form attributes"""
        model = acc_models.Profile
        fields = ['first_name', 'last_name', 'middle_initial', 'address', 'date_of_birth']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': main_const.ADDRESS_FIELD_PLACEHOLDER}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class ProfilePhoneNumberForm(forms.ModelForm):
    """A form to enter a phone number for a user"""
    class Meta:
        """ProfilePhoneNumber form attributes"""
        model = acc_models.ProfilePhoneNumbers
        fields = ['number_type', 'phone_number']
        widgets = {
            'number_type': forms.TextInput(attrs={'placeholder': acc_const.PHONE_NUMBER_TYPE_PLACEHOLDER}),
            'phone_number': forms.TextInput(attrs={'placeholder': main_const.PHONE_NUMBER_FIELD_PLACEHOLDER}),
        }


class ListVehicleForm(forms.ModelForm):
    """A form to list a vehicle"""
    class Meta:
        """Attributes of this form"""
        model = acc_models.List
        fields = ['address', 'car_value']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': main_const.ADDRESS_FIELD_PLACEHOLDER}),
        }


PhoneNumberFormset = formset_factory(ProfilePhoneNumberForm,
                                     min_num=acc_const.PHONE_NUMBER_FORMSET_MIN_NUM,
                                     validate_min=True,
                                     extra=acc_const.PHONE_NUMBER_FORMSET_EXTRA)
