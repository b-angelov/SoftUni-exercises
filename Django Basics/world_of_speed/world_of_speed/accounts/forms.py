from django import forms

from world_of_speed.accounts.models import Profile


class BaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

class CreateProfileForm(BaseForm):

    class Meta:
        model = Profile
        fields = ['username','email','age','password']