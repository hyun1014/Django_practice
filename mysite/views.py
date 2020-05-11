from django.shortcuts import render
from django.views.generic import TemplateView
from . import settings

class HomeView(TemplateView):
    template_name = 'home.html'