from django.urls import path
from .views import IndexView,URL_DetailView

app_name = 'bookmark'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', URL_DetailView.as_view(), name='urldetail'),
]
