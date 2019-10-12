from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Image


class ImageListView(ListView):
    '''
    class based view to display uploaded images
    '''
    model = Image
    template_name = 'main/index.html'
    context_object_name = 'images'
    ordering = ['-pk']

class ImageDetailView(DetailView):
    '''
    Class based view for viewing specific image with its details
    '''
    model = Image