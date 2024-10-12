

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import ProcessFormView

from fruitipedia.accounts.models import Profile
from fruitipedia.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipedia.fruits.models import Fruit


# Create your views here.

class DashboardView(ListView):
    template_name = 'fruits/dashboard.html'
    model = Fruit

class FruitCreateView(CreateView):
    model = Fruit
    template_name = 'fruits/create-fruit.html'
    form_class = CreateFruitForm

    def get_success_url(self):
        return reverse_lazy('dashboard_page')



class FruitDetailsView(DetailView):
    model = Fruit
    template_name = 'fruits/details-fruit.html'
    pk_url_kwarg = 'fruit_id'
    context_object_name = 'fruit'

class FruitEditView(UpdateView):
    model = Fruit
    template_name = 'fruits/edit-fruit.html'
    pk_url_kwarg = 'fruit_id'
    form_class = EditFruitForm

    def get_success_url(self):
        return reverse_lazy('dashboard_page')

class FruitDeleteView(DeleteView, UpdateView):
    model = Fruit
    template_name = 'fruits/delete-fruit.html'
    form_class = DeleteFruitForm
    pk_url_kwarg = 'fruit_id'

    def get_success_url(self):
        return reverse_lazy('dashboard_page')
