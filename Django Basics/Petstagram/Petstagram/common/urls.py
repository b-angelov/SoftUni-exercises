from django.urls import path

from Petstagram.common.views import index, like_functionality, copy_link_to_clipboard, add_comment

urlpatterns = [
    path('', index, name='home_page'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', add_comment, name='add_comment'),
]