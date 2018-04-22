# Forms used to create and add listed vehicles

from django import forms

from . import models as veh_models, constants as veh_const


class ChooseVehicleForm(forms.Form):
    """This class describes a form to choose a pre-existing vehicle"""
    vehicle = forms.ModelChoiceField(queryset=veh_models.Vehicle.objects.all())


class VehicleForm(forms.ModelForm):
    """This class describes a form to add a new vehicle to the database"""
    class Meta:
        """Form attributes"""
        model = veh_models.Vehicle
        fields = ['vehicle_type', 'weight']
        widgets = {
            'vehicle_type': forms.TextInput(attrs={'placeholder': veh_const.VEHICLE_TYPE_PLACEHOLDER}),
        }
