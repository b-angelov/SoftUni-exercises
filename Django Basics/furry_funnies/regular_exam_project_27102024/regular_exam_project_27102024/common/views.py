from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from regular_exam_project_27102024.posts.models import Post


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'common/index.html'

class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
