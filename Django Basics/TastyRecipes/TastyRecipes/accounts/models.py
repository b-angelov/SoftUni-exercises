from django.core.validators import MinLengthValidator
from django.db import models

from TastyRecipes.recipes.validators import FirstCapital


# Create your models here.

class Profile(models.Model):
    nickname = models.CharField(unique=True, max_length=20, null=False, blank=False, validators=(MinLengthValidator(2, message="Nickname must be at least 2 chars long!"),))
    first_name = models.CharField(max_length=30, null=False, blank=False, validators=(FirstCapital(),))
    last_name = models.CharField(max_length=30, null=False, blank=False, validators=(FirstCapital(),))
    chef = models.BooleanField(blank=False, null=False, default=False)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def get_last_profile():
        return Profile.objects.order_by('pk').last()

    def profile_full_name(self):
        return f'{self.first_name} {self.last_name}'
