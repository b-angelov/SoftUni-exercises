from django.core.validators import MinLengthValidator
from django.db import models

from MyPlant.common.validators import FirstCapitalValidator


# Create your models here.

class NameField(models.CharField):

    def __init__(self,*args, **kwargs):
        kwargs.update({'null':False,
        'blank':False,
        'max_length':20,
        'validators':(FirstCapitalValidator(message="Your name must start with a capital letter!"),)})
        super().__init__(*args, **kwargs)


class Profile(models.Model):

    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(MinLengthValidator(2),),
    )

    first_name = NameField()

    last_name = NameField()

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

