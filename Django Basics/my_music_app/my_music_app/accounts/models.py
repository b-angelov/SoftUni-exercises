from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

# Create your models here.

class Profile(models.Model):

    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(MinLengthValidator(2),RegexValidator(r'^[a-zA-Z_]+$', message="Ensure this value contains only letters, numbers, and underscore.")),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(0),)
    )

    @staticmethod
    def get_last_profile():
        return Profile.objects.last()
