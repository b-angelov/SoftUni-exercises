from django import forms

from MyPlant.common.form_mixins import FormCapitalizingMixin, FormDisableMixin
from MyPlant.plants.models import Plant


class BasePlantForm(forms.ModelForm, FormCapitalizingMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_capitalize(self.fields.values())

    class Meta:
        model = Plant
        fields = '__all__'
        abstract = True




class CreatePlantForm(BasePlantForm):
    pass

class DeletePlantForm(FormDisableMixin, BasePlantForm):
    pass