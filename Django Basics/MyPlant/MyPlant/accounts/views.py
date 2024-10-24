from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MyPlant.accounts.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm
from MyPlant.accounts.models import Profile
from MyPlant.plants.models import Plant

class ProfileObjectMixin:

    def get_object(self, queryset=None):
        return Profile.objects.last()

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'accounts/create-profile.html'
    success_url = reverse_lazy('plant-catalogue')

class ProfileDetailsView(ProfileObjectMixin,DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants = Plant.objects.count()
        plants = plants if plants < 3 else 3
        context['stars'] = range(plants)
        print(context['stars'])
        return context


class ProfileEditView(ProfileObjectMixin,UpdateView):
    model = Profile
    success_url = reverse_lazy('profile-details')
    form_class = ProfileEditForm
    template_name = 'accounts/edit-profile.html'



class ProfileDeleteView(ProfileObjectMixin,DeleteView):
    model=Profile
    success_url = reverse_lazy('home-page')
    template_name = 'accounts/delete-profile.html'
