from django.urls import path, include

from fruitipedia.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
]
