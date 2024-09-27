from django import forms

from Petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [ "name", "date_of_birth", "personal_pet_photo"]
        labels = {
            "personal_pet_photo": "Link to Image",
            "date_of_birth": "Date of Birth",
            "name": "Pet Name",
        }

        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Pet Name"}),
            'personal_pet_photo': forms.TextInput(attrs={"placeholder": "Link to image"}),
            'date_of_birth': forms.DateInput(attrs={"type": "date"}),
        }


class PetFormDisabled(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
            self.fields[field].readonly = 'readonly'


