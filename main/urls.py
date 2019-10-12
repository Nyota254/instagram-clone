from django.urls import re_path
from .views import ImageListView
from . import views

urlpatterns = [
    re_path(r'^$',ImageListView.as_view(),name="home_view")
]