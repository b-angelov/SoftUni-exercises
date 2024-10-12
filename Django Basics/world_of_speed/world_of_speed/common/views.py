from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from world_of_speed.accounts.models import Profile


# Create your views here.

class HomePage(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.last()
        return context

