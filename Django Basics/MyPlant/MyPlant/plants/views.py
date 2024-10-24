from django.forms import BaseForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.views.generic.edit import BaseFormView, BaseUpdateView

from MyPlant.plants.forms import CreatePlantForm, DeletePlantForm
from MyPlant.plants.models import Plant, PlantChoices


# Create your views here.

class PlantCatalogueView(ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'plants'

class PlantCreateView(CreateView):
    form_class = CreatePlantForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('plant-catalogue')


class PlantEditView(UpdateView):
    form_class = CreatePlantForm
    template_name = 'plants/edit-plant.html'
    success_url = reverse_lazy('plant-catalogue')
    model = Plant
    pk_url_kwarg = 'plant_id'

class PlantDeleteView(DeleteView, BaseUpdateView):
    form_class = DeletePlantForm
    template_name = 'plants/delete-plant.html'
    success_url = reverse_lazy('plant-catalogue')
    model = Plant
    pk_url_kwarg = 'plant_id'

    def form_invalid(self, form):
        return super().form_valid(form)


class PlantDetailsView(DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'
    pk_url_kwarg = 'plant_id'
