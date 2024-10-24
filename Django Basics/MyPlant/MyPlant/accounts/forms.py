from django import forms

from MyPlant.accounts.models import Profile
from MyPlant.common.form_mixins import FormCapitalizingMixin, FormDisableMixin


class BaseProfileForm(forms.ModelForm, FormCapitalizingMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_capitalize(self.fields.values())

    class Meta:
        abstract = True
        model = Profile
        fields = '__all__'

class ProfileCreateForm(BaseProfileForm):

    class Meta(BaseProfileForm.Meta):
        fields = ['username','first_name','last_name']

class ProfileEditForm(BaseProfileForm):
    pass

class ProfileDeleteForm(FormDisableMixin, BaseProfileForm):
    pass

