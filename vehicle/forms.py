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
        fields = ['description', 'weight']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': veh_const.VEHICLE_TYPE_PLACEHOLDER}),
        }


class VehicleTypeForm(forms.Form):
    """A form to choose the type of Vehicle"""
    vehicle_type = forms.ChoiceField(choices=veh_const.VEHICLE_TYPE_CHOICES, required=False)


class ChooseSedanForm(forms.Form):
    """A form to choose a pre-existing Sedan"""
    sedan = forms.ModelChoiceField(queryset=veh_models.Sedan.objects.all())


class SedanForm(forms.ModelForm):
    """A form to fill out information for a Sedan"""
    class Meta:
        """Form attributes"""
        model = veh_models.Sedan
        fields = ['sedan_class']


class ChooseTruckForm(forms.Form):
    """A form to choose a pre-existing Sedan"""
    truck = forms.ModelChoiceField(queryset=veh_models.Truck.objects.all())


class TruckForm(forms.ModelForm):
    """A form to fill out information for a Truck"""
    class Meta:
        """Form attributes"""
        model = veh_models.Truck
        fields = ['truck_bed_length', 'truck_bed_width']


class ChooseCoupeForm(forms.Form):
    """A form to choose a pre-existing Sedan"""
    coupe = forms.ModelChoiceField(queryset=veh_models.Coupe.objects.all())


class CoupeForm(forms.ModelForm):
    """A form to fill out information for a Coupe"""
    class Meta:
        """Form attributes"""
        model = veh_models.Coupe
        fields = ['top_style']


class ChooseSUVForm(forms.Form):
    """A form to choose a pre-existing Sedan"""
    suv = forms.ModelChoiceField(queryset=veh_models.SUV.objects.all())


class SUVForm(forms.ModelForm):
    """A form to fill out information for a SUV"""
    class Meta:
        """Form attributes"""
        model = veh_models.SUV
        fields = ['towing_capacity']
