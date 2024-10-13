from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from my_music_app.album.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from my_music_app.album.models import Album


# Create your views here.

class AlbumViewMixin:

    def get_success_url(self):
        return reverse_lazy('home_page')


class AlbumAddView(AlbumViewMixin,CreateView):
    model = Album
    template_name = 'album/album-add.html'
    form_class = CreateAlbumForm



class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-details.html'

class AlbumEditView(AlbumViewMixin,UpdateView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-edit.html'
    form_class = EditAlbumForm

    def get_success_url(self):
        return reverse_lazy('home_page')

class AlbumDeleteView(AlbumViewMixin,DeleteView,UpdateView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'
    form_class = DeleteAlbumForm
