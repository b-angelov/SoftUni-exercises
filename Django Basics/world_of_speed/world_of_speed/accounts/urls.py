from django.urls import path, include

from world_of_speed.accounts.views import ProfileCreate, ProfileDetails, ProfileEdit, ProfileDelete

urlpatterns = [
    path('', include([
        path('create/', ProfileCreate.as_view() ,name='profile create'),
        path('details/', ProfileDetails.as_view() ,name='profile details'),
        path('edit/', ProfileEdit.as_view() ,name='profile edit'),
        path('delete/', ProfileDelete.as_view() ,name='profile delete'),
    ]))
]
