from django.urls import path, include

from world_of_speed.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name="home page")
]
