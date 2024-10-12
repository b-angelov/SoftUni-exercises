from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import URLField

from fruitipedia.accounts.models import Profile
from fruitipedia.accounts.validators import IsAlphaValidator


# Create your models here.


class Fruit(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(MinLengthValidator(2),IsAlphaValidator(error_message=" Fruit name should contain only letters!")),
        error_messages={
            'unique': "This fruit name is already in use! Try a new one.",
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,

    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        editable=False,
    )
