from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):

    context = {

    }

    return render(request, 'home-page.html', context)
