from django.urls import path, include

from Petstagram.photos.views import photo_add, photo_details, photo_edit, photo_delete

urlpatterns = [
path('', include([
        path('add/', photo_add, name='photo_add_page'),
        path('<int:pk>/', photo_details, name='photo_details_page'),
        path('<int:pk>/edit/', photo_edit, name='photo_edit_page'),
        path('<int:pk>/delete/', photo_delete, name='photo_delete_page'),
    ])),
]