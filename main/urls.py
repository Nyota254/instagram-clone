from django.urls import re_path,path
from .views import (
    ImageListView,
    ImageDetailView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView,
    OtherProfile,
    ImageSearch
)


urlpatterns = [
    re_path(r'^$',ImageListView.as_view(),name="index_view"),
    re_path(r'^image/(?P<pk>\d+)$',ImageDetailView.as_view(),name="image_detail"),
    re_path(r'^image/new$',ImageCreateView.as_view(),name="image_upload"),
    re_path(r'^image/(?P<pk>\d+)/update',ImageUpdateView.as_view(),name="image_update"),
    re_path(r'^image/(?P<pk>\d+)/delete',ImageDeleteView.as_view(),name="image_delete"),
    re_path(r'^user/(?P<pk>\d+)',OtherProfile,name="single_profile"),
    re_path(r'^search/$',ImageSearch,name="search-results")
]