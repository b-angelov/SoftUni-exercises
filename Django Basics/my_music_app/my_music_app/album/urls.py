from django.urls import path, include

from my_music_app.album.views import AlbumAddView, AlbumDetailsView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('', include([
        path('add/', AlbumAddView.as_view(), name='album_add'),
        path('<int:id>/', include([
           path('details/', AlbumDetailsView.as_view(), name='album_details'),
           path('edit/', AlbumEditView.as_view(), name='album_edit'),
           path('delete/', AlbumDeleteView.as_view(), name='album_delete'),
        ])),
    ]))
]
