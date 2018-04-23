# Forms to collect data on the powertrain

from django import forms

from . import models as pow_models


class ChoosePowerTrainForm(forms.Form):
    """A form to choose pre-existing powertrain's"""
    powertrain = forms.ModelChoiceField(queryset=pow_models.PowerTrain.objects.all())


class PowerTrainForm(forms.ModelForm):
    """A form to add a new powertrain to the database"""
    class Meta:
        """Form Attributes"""
        model = pow_models.PowerTrain
        fields = ['model_number', 'drivetrain', 'engine_size']
