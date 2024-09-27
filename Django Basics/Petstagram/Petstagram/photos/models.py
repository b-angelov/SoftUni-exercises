from django.core.validators import MinLengthValidator
from django.db import models
from django.template.context_processors import static

from Petstagram.pets.models import Pet
from Petstagram.photos.validators import ValidateImageSize


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(validators=[ValidateImageSize()], upload_to="images")
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(to='pets.Pet', blank=True)
    date_of_publication = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_photos():
        return Photo.objects.prefetch_related('tagged_pets').all()

    @staticmethod
    def get_photo_by_id(pk):
        return Photo.objects.prefetch_related('tagged_pets').filter(pk=pk).first()

    @property
    def get_tagged_pets(self):
        return self.tagged_pets.all()

