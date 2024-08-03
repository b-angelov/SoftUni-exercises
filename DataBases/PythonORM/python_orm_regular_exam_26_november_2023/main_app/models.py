from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import AuthorManager


# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True)
    is_banned = models.BooleanField(default=False)
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    website = models.URLField(blank=True, null=True)

    objects = AuthorManager()

    def __str__(self):
        return self.full_name

class Article(models.Model):

    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = "Technology","Technology"
        SCIENCE = "Science","Science"
        EDUCATION = "Education","Education"

    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    content = models.TextField(validators=[MinLengthValidator(10)])
    category = models.CharField(max_length=10, default=CategoryChoices.TECHNOLOGY, choices = CategoryChoices)
    authors = models.ManyToManyField(to='Author')
    published_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField(validators=[MinLengthValidator(10)])
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE)
    published_on = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return self.content