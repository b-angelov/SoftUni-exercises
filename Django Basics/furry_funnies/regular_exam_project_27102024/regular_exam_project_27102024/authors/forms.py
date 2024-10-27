from django import forms

from regular_exam_project_27102024.authors.models import Author
from regular_exam_project_27102024.common.mixins import CapitalizeFormFieldLabelsMixin


class BaseAuthorForm(CapitalizeFormFieldLabelsMixin,forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = Author
        abstract = True
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    "placeholder":"Enter your first name..."
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    "placeholder":"Enter your last name..."
                }
            ),
            'passcode': forms.PasswordInput(
                attrs={
                    "placeholder":"Enter 6 digits...",
                }
            ),
            'pets_number': forms.NumberInput(
                attrs={
                    "placeholder":"Enter the number of your pets..." ,
                }
            ),
        }

class CreateAuthorForm(BaseAuthorForm):

    class Meta(BaseAuthorForm.Meta):
        exclude = ['info','image_url']

class EditAuthorForm(BaseAuthorForm):

    class Meta(BaseAuthorForm.Meta):
        exclude = ['passcode']
        help_texts ={
            'image_url':''
        }
        labels = {
            "image_url": "Profile Image URL"
        }
