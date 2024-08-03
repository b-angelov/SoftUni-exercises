from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import AstronautManager
from main_app.validators import DigitValidator


# Create your models here.


class Astronaut(models.Model):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    phone_number = models.CharField(max_length=15, validators=[DigitValidator(None,"Must contain digits only!")], unique=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateField(null=True, blank=True)
    spacewalks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    updated_at = models.DateTimeField(auto_now=True)

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(models.Model):
    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    manufacturer = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(validators=[MinValueValidator(1)])
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mission(models.Model):

    class StatusChoices(models.TextChoices):
        PLANNED = "Planned","Planned"
        ONGOING = "Ongoing","Ongoing"
        COMPLETED = "Completed","Completed"


    name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=9, default='Planned', choices=StatusChoices)
    launch_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    spacecraft = models.ForeignKey(to='Spacecraft', on_delete=models.CASCADE)
    astronauts = models.ManyToManyField(to='Astronaut')
    commander = models.ForeignKey(to='Astronaut', null=True, blank=True, on_delete=models.SET_NULL, related_name="commander")

    def __str__(self):
        return self.name