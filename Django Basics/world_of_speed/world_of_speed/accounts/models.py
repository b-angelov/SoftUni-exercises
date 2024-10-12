from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models
from django import forms
from django.db.models import Sum

from world_of_speed.accounts.validators import AlphaNumericUnderscoreValidator, ValueInRange


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(3), AlphaNumericUnderscoreValidator()],
        error_messages={
            'min_length': 'Username must be at least 3 chars long!',
        },
        null=False,
        blank=False,
    )

    email = models.EmailField(null=False, blank=False)

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(21)],
        help_text='Age requirement: 21 years and above.'
    )

    password = models.CharField(max_length=20)

    first_name = models.CharField(null=True, blank=True, max_length=25)

    last_name = models.CharField(null=True, blank=True, max_length=25)

    profile_picture = models.URLField(null=True, blank=True)

    @staticmethod
    def get_last_profile():
        return Profile.objects.last()

    @property
    def cars_total(self):
        return self.car_set.aggregate(Sum('price', default=0))['price__sum']




