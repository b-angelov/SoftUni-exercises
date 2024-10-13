from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from my_music_app.album.models import Album


# Create your views here.

class AlbumAddView(CreateView):
    model = Album
    template_name = 'album/album-add.html'
    fields='__all__'

class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-details.html'

class AlbumEditView(UpdateView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-edit.html'

class AlbumDeleteView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'
