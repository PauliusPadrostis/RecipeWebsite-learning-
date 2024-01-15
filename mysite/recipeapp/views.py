from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def homepage(request):
    return render(request, 'homepage.html', context={})

def about(request):
    return render(request, 'about.html', context={})