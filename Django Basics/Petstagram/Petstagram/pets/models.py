from django.db import models
from django.utils.text import slugify


# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_pet_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify([self.name,self.id])
        super().save(*args, **kwargs)

    @staticmethod
    def get_pet_by_slug(slug):
        return Pet.objects.filter(slug=slug).first()


