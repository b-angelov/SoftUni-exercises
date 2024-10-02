from django.urls import path

from TastyRecipes.common.views import home_page

urlpatterns =[
    path('', home_page, name='home'),
]