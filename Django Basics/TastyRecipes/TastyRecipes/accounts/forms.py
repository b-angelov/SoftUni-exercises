from django import forms

from TastyRecipes.accounts.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = [ 'bio']


class DeleteProfileForm(forms.Form):
    submit = forms.TextInput(attrs={
        'class': 'btn-submit',
        'value': 'Yes',
        'type': 'submit'
    })

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'