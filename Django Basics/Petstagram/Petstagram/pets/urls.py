from django.urls import path, include

from Petstagram.pets.views import pet_delete, pet_add, pet_edit, pet_details
urlpatterns = [
    path('', include([
        path('add/', pet_add, name='pet_add_page'),
        path('<str:username>/pet/<slug:pet_slug>/edit', pet_edit, name='pet_edit_page'),
        path('<str:username>/pet/<slug:pet_slug>/delete', pet_delete, name='pet_delete_page'),
        path('<str:username>/pet/<slug:pet_slug>/', pet_details, name='pet_details_page'),
    ])),
]

