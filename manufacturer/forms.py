# Forms used in junction with manufacturers

from django import forms
from django.forms import formset_factory

from carRepo import constants as main_const

from . import models as man_models, constants as man_const


class ChooseManufacturerForm(forms.Form):
    """A form to choose a pre-existing Manufacturer"""
    manufacturer = forms.ModelChoiceField(queryset=man_models.Manufacturer.objects.all())


class ManufacturerForm(forms.ModelForm):
    """A form to create a new manufacturer"""
    class Meta:
        """Form attributes"""
        model = man_models.Manufacturer
        fields = '__all__'
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': main_const.ADDRESS_FIELD_PLACEHOLDER}),
        }


class ManufacturerPhoneNumberForm(forms.ModelForm):
    """A form to create manufacturer phone numbers"""
    class Meta:
        """Form attributes"""
        model = man_models.ManufacturerPhoneNumbers
        fields = ['number_type', 'phone_number']
        widgets = {
            'number_type': forms.TextInput(attrs={'placeholder': man_const.PHONE_NUMBER_TYPE_PLACEHOLDER}),
            'phone_number': forms.TextInput(attrs={'placeholder': main_const.PHONE_NUMBER_FIELD_PLACEHOLDER}),
        }


PhoneNumberFormset = formset_factory(ManufacturerPhoneNumberForm,
                                     min_num=man_const.PHONE_NUMBER_MIN_NUM,
                                     extra=man_const.PHONE_NUMBER_EXTRA,
                                     validate_min=True)
