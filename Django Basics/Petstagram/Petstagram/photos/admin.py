from django.contrib import admin

from Petstagram.pets.models import Pet
from Petstagram.photos.models import Photo


# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','date_of_publication','description','get_tagged_pets']

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(pet.name for pet in obj.tagged_pets.all())
