from django import forms

from my_music_app.accounts.models import Profile


class BaseProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields='__all__'
        abstract=True

class CreateProfileForm(BaseProfileForm):

    class Meta(BaseProfileForm.Meta):
        fields = ['username','email','age']
