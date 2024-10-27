

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import BaseFormView

from regular_exam_project_27102024.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from regular_exam_project_27102024.posts.models import Post


# Create your views here.

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create-post.html'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse_lazy('dashboard')

class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'

class PostEditView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    form_class = EditPostForm

    def get_success_url(self):
        return reverse_lazy('dashboard')

class PostDeleteView(DeleteView, BaseFormView):
    model = Post
    form_class = DeletePostForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/delete-post.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)