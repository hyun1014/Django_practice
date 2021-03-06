from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('posts/', PostLV.as_view(), name='post_list'),
    path('posts/<slug:slug>/', PostDV.as_view(), name='post_detail'),
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>', PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>', PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>', PostDAV.as_view(), name='post_day_archive'),
    path('archive/today', PostTAV.as_view(), name='post_today_archive'),
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>', TaggedObjectLV.as_view(), name='tagged_object_list'),
]
