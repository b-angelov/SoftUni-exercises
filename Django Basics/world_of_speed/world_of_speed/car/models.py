from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from world_of_speed.accounts.models import Profile
from world_of_speed.accounts.validators import ValueInRange


# Create your models here.


class Car(models.Model):

    class TypeChoices(models.TextChoices):
        RALLY = "RY","Rally"
        OPEN_WHEEL = "OW","Open-wheel"
        KART = "KT","Kart"
        DRAG = "DG","Drag"
        OTHER = "OT","Other"

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices = TypeChoices
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=[MinLengthValidator(1)]
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[ValueInRange(1999,2030)]
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        help_text="https://...",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one.",
        }
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1.0)]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        editable=False
    )