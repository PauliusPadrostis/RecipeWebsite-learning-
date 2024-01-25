from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html', context={})


class AllRecipes(generic.ListView):
    model = Recipe
    template_name = 'all_recipes.html'
    context_object_name = 'recipes'
