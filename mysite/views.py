from django.shortcuts import render
from django.views.generic import View
from . import settings

class DefaultView(View):
    def onlyappname(self, st):
        return st.split('.')[0]
    def get(self, request):
        aaa = list(map(self.onlyappname, settings.INSTALLED_APPS[6:]))
        return render(request, 'base.html', {'applist': aaa})