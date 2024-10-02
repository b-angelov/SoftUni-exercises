from django import forms

from TastyRecipes.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'cuisine_type': 'Cuisine Type:',
            'image_url': 'Image URL:',
            'cooking_time': 'Cooking Time:'
        }

        help_texts = {
            # 'cooking_time':'Provide the cooking time in minutes.'
        }

        widgets = {
            'ingredients': forms.Textarea(
                attrs = {
                    'placeholder': "ingredient1, ingredient2, ...",
                }
            ),
            'instructions': forms.Textarea(
                attrs = {
                    'placeholder': "Enter detailed instructions here...",
                }
            ),
            'image_url': forms.URLInput(
                attrs = {
                    'placeholder': "Optional image URL here...",
                }
            )
        }

class DeleteRecipeForm(CreateRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
            self.fields[field].readonly = 'readonly'