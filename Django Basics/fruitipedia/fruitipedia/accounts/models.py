from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from fruitipedia.accounts.validators import FirstAlphaValidator


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=(MinLengthValidator(2), FirstAlphaValidator()),
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=(MinLengthValidator(1), FirstAlphaValidator(error_message="Your name must start with a letter!")),
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        max_length=40
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=(MinLengthValidator(8),),
        help_text="*Password length requirements: 8 to 20 characters"
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )

    @staticmethod
    def get_last_profile():
        return Profile.objects.last()

