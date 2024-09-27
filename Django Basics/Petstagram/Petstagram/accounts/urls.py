from django.urls import path, include
from Petstagram.accounts.views import register, login, profile_details, profile_edit, profile_delete

urlpatterns = [

    path('', include([
        path('register/',register, name='register_page'),
        path('login/',login, name='login_page'),
        path('profile/<int:pk>/',profile_details, name='profile_page'),
        path('profile/<int:pk>/edit',profile_edit, name='profile_edit_page'),
        path('profile/<int:pk>/delete',profile_delete, name='profile_delete_page'),
    ])),
]