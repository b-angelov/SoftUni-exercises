from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import TextChoices

from TastyRecipes.accounts.models import Profile
from TastyRecipes.recipes.validators import FirstCapital


# Create your models here.


class Recipe(models.Model):

    class CuisineChoices(TextChoices):
        FRENCH = 'FR', 'French'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        BALKAN = 'BK', 'Balkan'
        OTHER = 'OT', 'Other'


    title = models.CharField(null=False, blank=False, unique=True, max_length=100, validators=(MinLengthValidator(10),),
                             error_messages={
                                 'unique': '"We already have a recipe with the same title!"'
                             })
    cuisine_type = models.CharField(max_length=7, blank=False, null=False, choices=CuisineChoices)
    ingredients = models.TextField(blank=False, null=False, help_text="Ingredients must be separated by a comma and space.")
    instructions = models.TextField(blank=False, null=False)
    cooking_time = models.PositiveIntegerField(blank=False, null=False, validators=(MinValueValidator(1),), help_text="Provide the cooking time in minutes.")
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, editable=False)



