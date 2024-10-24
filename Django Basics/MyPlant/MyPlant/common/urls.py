from django.urls import path, include

from MyPlant.common.views import HomePageView
from MyPlant.plants.views import PlantCatalogueView, PlantCreateView, PlantEditView, PlantDeleteView, PlantDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('catalogue/', PlantCatalogueView.as_view(), name='plant-catalogue'),
    path('create/', PlantCreateView.as_view(), name='plant-create'),
    path('details/<int:plant_id>/', PlantDetailsView.as_view(), name='plant-details'),
    path('edit/<int:plant_id>/', PlantEditView.as_view(), name='plant-edit'),
    path('delete/<int:plant_id>/', PlantDeleteView.as_view(), name='plant-delete'),
]
