from django.urls import path, include

from fruitipedia.fruits.views import FruitCreateView, FruitDetailsView, FruitEditView, FruitDeleteView

urlpatterns = [
    path('create/', FruitCreateView.as_view(), name='create_fruit'),
    path('<int:fruit_id>/', include([
        path('details/', FruitDetailsView.as_view(), name='details_fruit'),
        path('edit/', FruitEditView.as_view(), name='edit_fruit'),
        path('delete/', FruitDeleteView.as_view(), name='delete_fruit'),
    ])
         ),
]
