from django.urls import path, include

from my_music_app.accounts.views import ProfileDetailsView, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
