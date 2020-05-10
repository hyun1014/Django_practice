from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.SelectView.as_view(), name='select'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:pk>/result', views.ResultView.as_view(), name='result'),
]
