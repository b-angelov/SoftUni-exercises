from django.forms import ModelForm, TextInput, Textarea
from prompt_toolkit.widgets import TextArea

from fruitipedia.accounts.models import Profile
from fruitipedia.fruits.models import Fruit


class BaseFruitForm(ModelForm):


    def save(self, commit=True):
        object = super().save(commit=False)
        object.owner_id = Profile.get_last_profile().pk
        object.save()

    class Meta:
        model = Fruit
        fields = '__all__'
        abstract = True
        labels = {
            'name':'',
            'image_url':'',
            'description':'',
            'nutrition':''
        }

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':"Fruit Name"
                }
            ),
            'image_url': TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder':'Fruit Description'
                }
            ),
            'nutrition': Textarea(
                attrs={
                    'placeholder':'Nutrition Info'
                }
            )
        }

class CreateFruitForm(BaseFruitForm):

    class Meta(BaseFruitForm.Meta):
        pass

class EditFruitForm(BaseFruitForm):

    class Meta(BaseFruitForm.Meta):
        labels = {}

class DeleteFruitForm(BaseFruitForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
