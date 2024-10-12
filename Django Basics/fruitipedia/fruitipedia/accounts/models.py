from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Model(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=(MinLengthValidator(2),),
    )
