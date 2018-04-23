# Forms used to create and add listed vehicles

from django import forms

from . import models as veh_models, constants as veh_const


class ChooseVehicleForm(forms.Form):
    """This class describes a form to choose a pre-existing vehicle"""
    sedans = forms.ModelChoiceField(queryset=veh_models.Sedan.objects.all(), required=False)
    trucks = forms.ModelChoiceField(queryset=veh_models.Truck.objects.all(), required=False)
    coupes = forms.ModelChoiceField(queryset=veh_models.Coupe.objects.all(), required=False)
    suvs = forms.ModelChoiceField(queryset=veh_models.SUV.objects.all(), required=False)
    other_vehicles = forms.ModelChoiceField(queryset=veh_models.Vehicle.objects.all(), required=False)


class VehicleForm(forms.ModelForm):
    """This class describes a form to add a new vehicle to the database"""
    class Meta:
        """Form attributes"""
        model = veh_models.Vehicle
        fields = ['description', 'weight']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': veh_const.VEHICLE_TYPE_PLACEHOLDER}),
            'weight': forms.TextInput(attrs={'placeholder': veh_const.VEHICLE_WEIGHT_PLACEHOLDER}),
        }


class VehicleTypeForm(forms.Form):
    """A form to choose the type of Vehicle"""
    vehicle_type = forms.ChoiceField(choices=veh_const.VEHICLE_TYPE_CHOICES, required=False)


class SedanForm(forms.ModelForm):
    """A form to fill out information for a Sedan"""
    class Meta:
        """Form attributes"""
        model = veh_models.Sedan
        fields = ['sedan_class']


class TruckForm(forms.ModelForm):
    """A form to fill out information for a Truck"""
    class Meta:
        """Form attributes"""
        model = veh_models.Truck
        fields = ['truck_bed_length', 'truck_bed_width']
        widgets = {
            'truck_bed_width': forms.TextInput(attrs={'placeholder': veh_const.TRUCK_BED_LENGTH_AND_WIDTH_PLACEHOLDER}),
            'truck_bed_length': forms.TextInput(
                attrs={'placeholder': veh_const.TRUCK_BED_LENGTH_AND_WIDTH_PLACEHOLDER}),
        }


class CoupeForm(forms.ModelForm):
    """A form to fill out information for a Coupe"""
    class Meta:
        """Form attributes"""
        model = veh_models.Coupe
        fields = ['top_style']


class SUVForm(forms.ModelForm):
    """A form to fill out information for a SUV"""
    class Meta:
        """Form attributes"""
        model = veh_models.SUV
        fields = ['towing_capacity']
        widgets = {
            'towing_capacity': forms.TextInput(attrs={'placeholder': veh_const.SUV_TOWING_CAPACITY_PLACEHOLDER}),
        }
