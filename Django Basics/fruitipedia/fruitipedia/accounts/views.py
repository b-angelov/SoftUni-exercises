from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.accounts.forms import CreateProfileForm
from fruitipedia.accounts.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'accounts/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard_page')

class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/details-profile.html'

class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'accounts/edit-profile.html'

class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/delete-profile.html'