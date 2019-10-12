from django.urls import re_path
from .views import (
    ImageListView,
    ImageDetailView,
    ImageCreateView
)
from . import views

urlpatterns = [
    re_path(r'^$',ImageListView.as_view(),name="home_view"),
    re_path(r'^image/(?P<pk>\d+)',ImageDetailView.as_view(),name="image_detail"),
    re_path(r'^image/new$',ImageCreateView.as_view(),name="image_upload")
]