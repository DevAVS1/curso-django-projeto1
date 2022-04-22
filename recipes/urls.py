from django.urls import path

from recipes.views import my_recipes, my_view

urlpatterns = [
    path('', my_view),
    path('receitas', my_recipes)
]
