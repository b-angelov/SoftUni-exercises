from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models

from main_app.managers import TennisPlayerManager
from main_app.validators import RangeLengthValidator, RangeValueValidator


# Create your models here.


class TennisPlayer(models.Model):
    full_name = models.CharField(max_length=120, validators=[RangeLengthValidator(5,120)])
    birth_date = models.DateField()
    country = models.CharField(max_length=100,validators=[RangeLengthValidator(2,100)])
    ranking = models.PositiveIntegerField(validators=[RangeValueValidator(1,300)])
    is_active = models.BooleanField(default=True)

    objects = TennisPlayerManager()

    def __str__(self):
        return self.full_name


class Tournament(models.Model):

    class SurfaceTypesChoices(models.TextChoices):
        NOT_SELECTED = "Not Selected","Not Selected"
        CLAY = "Clay","Clay"
        GRASS = "Grass","Grass"
        HARD_COURT = "Hard Court","Hard Court"

    name = models.CharField(max_length=150,unique=True, validators=[RangeLengthValidator(2, 150)])
    location = models.CharField(max_length=100,validators=[RangeLengthValidator(2,100)])
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    surface_type = models.CharField(max_length=12, default='Not Selected', choices=SurfaceTypesChoices)

    def __str__(self):
        return self.name


class Match(models.Model):
    score = models.CharField(max_length=100)
    summary = models.TextField(validators=[MinLengthValidator(5)])
    date_played = models.DateTimeField()
    tournament = models.ForeignKey(to='Tournament', on_delete=models.CASCADE)
    players = models.ManyToManyField(to='TennisPlayer', related_name='matches')
    winner = models.ForeignKey(to='TennisPlayer', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Matches'