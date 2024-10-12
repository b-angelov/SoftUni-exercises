from django.urls import path, include

from world_of_speed.car.views import CarCatalogue, CarCreate, CarDetails, CarEdit, CarDelete

urlpatterns = [
    path('', include([
        path('catalogue/', CarCatalogue.as_view(), name='car catalogue'),
        path('create/', CarCreate.as_view(), name='car create'),
        path('<int:pk>/',include([
            path('details/', CarDetails.as_view(), name='car details'),
            path('edit/', CarEdit.as_view(), name='car edit'),
            path('delete/', CarDelete.as_view(), name='car delete'),
        ]))
    ])),
]
