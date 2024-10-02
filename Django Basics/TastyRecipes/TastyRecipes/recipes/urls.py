from django.urls import path, include

from TastyRecipes.recipes.views import catalogue_page, create_recipe, recipe_details, recipe_edit, recipe_delete

urlpatterns =[
    path('',include([
        path('catalogue/', catalogue_page, name='catalogue'),
        path('create/', create_recipe, name='create_recipe'),
        path('<int:recipe_id>/', include([
            path('details/', recipe_details, name='recipe_details'),
            path('edit/', recipe_edit, name='recipe_edit'),
            path('delete/', recipe_delete, name='recipe_delete'),
        ])),
    ]),
         )
]