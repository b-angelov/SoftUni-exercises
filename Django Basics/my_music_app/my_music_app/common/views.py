from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from my_music_app.accounts.forms import CreateProfileForm
from my_music_app.album.models import Album


# Create your views here.


class HomePageView(TemplateView, FormView):
    template_name = 'common/home.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return self.render_to_response(self.get_context_data())


