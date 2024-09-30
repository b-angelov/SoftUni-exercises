from django.urls import path, include

from Petstagram.pets.views import pet_delete, pet_add, pet_edit, pet_details, AddPetView, PetDetailsView, EditPetView, \
    DeletePetView

urlpatterns = [
    path('', include([
        path('add/', AddPetView.as_view(), name='pet_add_page'),
        path('<str:username>/pet/<slug:pet_slug>/edit', EditPetView.as_view(), name='pet_edit_page'),
        path('<str:username>/pet/<slug:pet_slug>/delete', DeletePetView.as_view(), name='pet_delete_page'),
        path('<str:username>/pet/<slug:pet_slug>/', PetDetailsView.as_view(), name='pet_details_page'),
    ])),
]

