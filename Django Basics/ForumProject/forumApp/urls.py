from django.template.defaulttags import url
from django.urls import path, include

from forumApp.views import index, dashboard, article, posts

urlpatterns = [
    path('',index,name='index'),
    path('dashboard/', include(
        [
            path('', dashboard, name='dashboard'),
            path(f'posts/<int:pk>/<slug:title>', posts, name='post'),
        ]
    )),
    path(f'articles/<slug:title>', article, name='article_details'),
    path(f'posts/<int:pk>/<slug:title>', posts, name='post_details'),
]