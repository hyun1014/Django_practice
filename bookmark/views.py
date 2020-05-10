from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark
from mysite import settings
# Create your views here.
def onlyappname(st):
        return st.split('.')[0]

applist = list(map(onlyappname, settings.INSTALLED_APPS[6:]))


class IndexView(ListView):
    template_name = 'bookmark/index.html'
    def get_queryset(self):
        return Bookmark.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applist"] = applist
        return context
    


class URL_DetailView(DetailView):
    model = Bookmark
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["applist"] = applist
        return context
    