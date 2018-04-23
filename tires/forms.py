# Forms to collect data on tires

from django import forms

from . import models as tire_models


class ChooseTiresForm(forms.Form):
    """A form to choose from current tires in the database"""
    tires = forms.ModelChoiceField(queryset=tire_models.Tires.objects.all())


class TiresForm(forms.ModelForm):
    """A form to add a new type of tires to the database"""
    class Meta:
        """Form attributes"""
        model = tire_models.Tires
        fields = ['model_number', 'description']
