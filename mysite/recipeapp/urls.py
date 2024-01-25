from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_recipes/', views.AllRecipes.as_view(), name='all_recipes')
]