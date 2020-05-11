from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark
from mysite import settings
# Create your views here.

class IndexView(ListView):
    template_name = 'bookmark/index.html'
    def get_queryset(self):
        return Bookmark.objects.all()
    


class URL_DetailView(DetailView):
    model = Bookmark