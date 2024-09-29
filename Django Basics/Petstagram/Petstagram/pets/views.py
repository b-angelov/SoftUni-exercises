from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from parso.python.tree import Class



# Create your views here.

class ClassImporter:
    @property
    def Pet(self):
        from Petstagram.pets.models import Pet
        return Pet

    @property
    def PetForm(self):
        from Petstagram.pets.forms import PetForm
        return PetForm

    @property
    def CommentForm(self):
        from Petstagram.common.forms import CommentForm
        return CommentForm



class AddPetView(CreateView):

    model = ClassImporter.Pet
    form_class = ClassImporter.PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile_page', kwargs={'pk':1})


class PetDetailsView(DetailView):

    COMMENT_FORM = ClassImporter.CommentForm
    model = ClassImporter.Pet
    template_name = "pets/pet-details-page.html"
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_photos"] = self.object.photo_set.all()
        context["comment_form"] = self.COMMENT_FORM()
        return context


class EditPetView(UpdateView):

    model = ClassImporter.Pet
    form_class = ClassImporter.PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        self.object.save()
        return reverse_lazy(
            'pet_details_page',
            kwargs={
                'username':self.kwargs['username'],
                # 'pet_slug': slugify(self.object.name + " " + str(self.object.pk)),
                'pet_slug': slugify(self.object.slug),
            }
        )


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
    from Petstagram.common.forms import CommentForm

    Pet = apps.get_model('pets','Pet')
    pet = Pet.get_pet_by_slug(pet_slug)
    comment_form = CommentForm(request.POST or None)

    context = {
        'pet':pet,
        'pet_photos': pet.photo_set.all(),
        'comment_form':comment_form,
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
