from decimal import Decimal

from django.contrib.postgres.search import SearchVectorField
from django.core.validators import MinValueValidator, EmailValidator, URLValidator, MinLengthValidator
from django.db import models

from main_app.mixins import RechargeEnergyMixin
from main_app.validators import ValidName, CountryPhoneNumberValidator


# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=100, validators = [ValidName()])
    age = models.PositiveIntegerField(validators = [MinValueValidator(18,"Age must be greater than or equal to 18")])
    email = models.EmailField(error_messages={'invalid': 'Enter a valid email address'})
    phone_number = models.CharField(max_length=13, validators=[CountryPhoneNumberValidator()])
    website_url = models.URLField(error_messages={'invalid':"Enter a valid URL"})


class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created_at','title']

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

class Book(BaseMedia):
    author = models.CharField(max_length=100, validators=[MinLengthValidator(5,"Author must be at least 5 characters long")])
    isbn = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(6,  "ISBN must be at least 6 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'


class Movie(BaseMedia):
    director = models.CharField(max_length=100, validators=[MinLengthValidator(8, "Director must be at least 8 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'


class Music(BaseMedia):
    artist = models.CharField(max_length=100, validators=[MinLengthValidator(9, "Artist must be at least 9 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return self.price * Decimal(0.08)

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal(2.00)

    def format_product_name(self):
        return f"Product: {self.name}"



class DiscountedProduct(Product):

    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return self.price * Decimal(1.20)

    def calculate_tax(self):
        return self.price * Decimal(0.05)

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal(1.50)

    def format_product_name(self):
        return f'Discounted Product: {self.name}'


class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        try:
            energy = self.__energy
            energy = value
            if energy < 0:
                raise ValueError('cannot decrease below zero')
            self.__energy = energy
        except AttributeError:
            self.__energy = value
        self.__energy = min(100, self.__energy)


class SpiderHero(Hero):

    def swing_from_buildings(self):
        try:
            self.energy -= 80
        except ValueError:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        self.energy = max(1,self.energy)
        self.clean()
        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"

    class Meta:
        proxy = True


class FlashHero(Hero):

    def run_at_super_speed(self):
        try:
            self.energy -= 65
        except ValueError:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        self.energy = max(1, self.energy)
        self.clean()
        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"

    class Meta:
        proxy=True


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['search_vector'])
        ]




