# Set up the Crispy forms for all forms in project.

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class CrispyModelForm(forms.ModelForm):
    """Crispy settings for a model form"""
    def __init__(self, *args, **kwargs):
        """initialize crispy form"""
        super(CrispyModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
