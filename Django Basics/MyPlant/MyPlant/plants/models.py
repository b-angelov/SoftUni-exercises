from django.core.validators import MinLengthValidator
from django.db import models

from MyPlant.common.validators import IsAlphaValidator


# Create your models here.

class PlantChoices(models.TextChoices):
    INDOOR_PLANTS = '1', 'Indoor Plants',
    OUTDOOR_PLANTS =  '2', 'Outdoor Plants'

class Plant(models.Model):

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=PlantChoices
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(MinLengthValidator(2),IsAlphaValidator("Plant name should contain only letters!"))
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
