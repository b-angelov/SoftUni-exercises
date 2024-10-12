from django import forms

from world_of_speed.accounts.models import Profile
from world_of_speed.car.models import Car


class CarBaseForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        disabled = kwargs.pop('disable') if 'disable' in kwargs else False
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label.capitalize()
            if disabled and (disabled == '__all__' or field in disabled):
                self.fields[field].disabled = True
                self.fields[field].widget.attrs["readonly"] = 'readonly'
            if field == 'image_url':
                self.fields[field].label = 'ImageURL'
                self.fields[field].help_text = ''

    class Meta:
        model = Car
        fields = ['type','model','year','image_url','price']
        widgets = {
            'image_url':forms.URLInput(attrs={
                'placeholder':'http://...',
            })
        }

    def save(self, commit=True):
        form = super().save(commit=False)
        form.owner_id = Profile.get_last_profile().pk
        return form.save()

class CarCreateForm(CarBaseForm):
    pass

class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        kwargs['disable'] = '__all__'
        super().__init__(*args, **kwargs)