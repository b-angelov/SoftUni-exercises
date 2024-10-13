from django.core.validators import MinValueValidator
from django.db import models
from django.forms import PasswordInput

from my_music_app.accounts.models import Profile


# Create your models here.


class Album(models.Model):

    class GenreChoices(models.TextChoices):
        POP_MUSIC = "PM","Pop Music"
        JAZZ_MUSIC = "JM","Jazz Music"
        R_AND_B_MUSIC = "RBM","R&B Music"
        ROCK_MUSIC = "RM","Rock Music"
        COUNTRY_MUSIC = "CM","Country Music"
        DANCE_MUSIC = "DM","Dance Music"
        HIP_HOP_MUSIC = "HHM","Hip Hop Music"
        OTHER = 'O',"Other"

    album_name = models.CharField(
        unique=True,
        max_length=30
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=GenreChoices
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(0.0),)
    )

    owner = models.ForeignKey(
        to=Profile,
        editable=False,
        on_delete=models.CASCADE
    )
