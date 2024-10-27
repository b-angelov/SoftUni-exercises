from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from regular_exam_project_27102024.authors.forms import CreateAuthorForm, EditAuthorForm
from regular_exam_project_27102024.authors.models import Author
from regular_exam_project_27102024.common.mixins import DefaultProfileMixin
from regular_exam_project_27102024.utils.get_profile import get_profile


# Create your views here.

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'authors/create-author.html'
    form_class = CreateAuthorForm

    def get_success_url(self):
        return reverse_lazy('dashboard')

class AuthorDetailsView(DefaultProfileMixin,DetailView):
    model = Author
    template_name = 'authors/details-author.html'


class AuthorEditView(DefaultProfileMixin,UpdateView):
    model = Author
    template_name = 'authors/edit-author.html'
    form_class = EditAuthorForm

    def get_success_url(self):
        return reverse_lazy('author_details')

class AuthorDeleteView(DefaultProfileMixin,DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'

    def get_success_url(self):
        return reverse_lazy('home-page')