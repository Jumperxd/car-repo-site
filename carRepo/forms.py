# Set up the Crispy forms for all forms in project.

from account import constants as acc_const

from django import forms

from vehicle import constants as veh_const

from . import constants as main_const


class AdvancedSearchForm(forms.Form):
    """A form to collect search parameters"""
    username = forms.CharField(max_length=main_const.USERNAME_MAX_LENGTH, required=False)
    address = forms.CharField(max_length=acc_const.LIST_ADDRESS_MAX_LENGTH,
                              help_text=main_const.ADDRESS_HELP_TEXT,
                              required=False)
    maximum_price = forms.DecimalField(max_digits=acc_const.LIST_CAR_VALUE_MAX_DIGITS,
                                       decimal_places=acc_const.LIST_CAR_VALUE_DECIMAL_PLACES,
                                       required=False)
    vehicle_type = forms.ChoiceField(choices=veh_const.VEHICLE_TYPE_CHOICES, required=False)
