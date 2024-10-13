from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.accounts.forms import CreateProfileForm
from fruitipedia.accounts.models import Profile


# Create your views here.

class ProfileViewMixin:

    def get_object(self, *args, **kwargs):
        return self.model.get_last_profile()


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'accounts/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard_page')

class ProfileDetailsView(ProfileViewMixin,DetailView):
    model = Profile
    template_name = 'accounts/details-profile.html'
    query_pk_and_slug = False



class ProfileEditView(ProfileViewMixin,UpdateView):
    model = Profile
    template_name = 'accounts/edit-profile.html'
    success_url = reverse_lazy('details_profile')
    fields = ['first_name','last_name','image_url','age']

class ProfileDeleteView(ProfileViewMixin,DeleteView):
    model = Profile
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('home_page')