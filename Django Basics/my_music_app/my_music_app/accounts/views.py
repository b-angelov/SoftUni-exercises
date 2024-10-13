from django.shortcuts import render
from django.views.generic import DetailView, DeleteView

from my_music_app.accounts.models import Profile


# Create your views here.
class ProfileBaseMixin:

    def get_object(self,*args,**kwargs):
        return Profile.get_last_profile()


class ProfileDetailsView(ProfileBaseMixin,DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'

class ProfileDeleteView(ProfileBaseMixin,DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'


