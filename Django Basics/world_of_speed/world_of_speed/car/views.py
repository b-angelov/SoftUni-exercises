from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from world_of_speed.car.forms import CarCreateForm, CarDeleteForm
from world_of_speed.car.models import Car


# Create your views here.

class CarCatalogue(ListView):
    model=Car
    fields = '__all__'
    template_name = 'car/catalogue.html'

class CarCreate(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'

    def get_success_url(self):
        return reverse('car catalogue')

class CarDetails(DetailView):
    model=Car
    template_name = 'car/car-details.html'

class CarEdit(UpdateView):
    model=Car
    template_name = 'car/car-edit.html'
    form_class = CarCreateForm

    def get_success_url(self):
        return reverse_lazy('car catalogue')

class CarDelete(DeleteView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarDeleteForm(initial=Car.objects.get(pk=self.object.pk).__dict__)
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        return self.form_valid(self.get_form())


    model = Car
    template_name = 'car/car-delete.html'
    form_class = CarDeleteForm

    def get_success_url(self):
        return reverse_lazy('car catalogue')
