from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify



# Create your views here.



def pet_add(request):
    from Petstagram.pets.forms import PetForm
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile_page', 1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)

def pet_details(request,username,pet_slug):
    Pet = apps.get_model('pets','Pet')
    pet = Pet.get_pet_by_slug(pet_slug)

    context = {
        'pet':pet,
        'pet_photos': pet.photo_set.all()
    }

    return render(request, 'pets/pet-details-page.html', context)

def pet_edit(request, username, pet_slug):
    from Petstagram.pets.forms import PetForm
    from Petstagram.pets.models import Pet

    pet = Pet.objects.get(slug=pet_slug)

    def get():
        form = PetForm(instance=pet, initial=pet.__dict__)
        return form

    def post():
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_details_page', username, pet.slug)

    form = {"GET":get}.get(request.method, post)()
    if isinstance(form, HttpResponse):
        return form

    context = {
        "form":form,
    }

    return render(request, 'pets/pet-edit-page.html', context)

def pet_delete(request, username, pet_slug):
    from Petstagram.pets.forms import PetFormDisabled
    from Petstagram.pets.models import Pet

    pet = Pet.get_pet_by_slug(pet_slug)

    if request.method == "GET":
        form = PetFormDisabled(instance=pet)
    else:
        form = PetFormDisabled(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()
            return redirect('profile_page', pk=1)

    context = {
        "form":form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
