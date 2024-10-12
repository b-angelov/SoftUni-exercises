from django.forms import ModelForm, BaseModelForm, PasswordInput

from fruitipedia.accounts.models import Profile


class BaseProfileForm(ModelForm):

    class Meta:
        fields = '__all__'
        model = Profile
        abstract=True
        widgets = {
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            )
        }
        labels = {
            'password':'',
        }


class CreateProfileForm(BaseProfileForm):

    class Meta(BaseProfileForm.Meta):
        fields = ['first_name','last_name','email','password']