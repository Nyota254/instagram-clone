from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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

class ImageCreateView(LoginRequiredMixin,CreateView):
    '''
    Class based view for adding new image
    '''
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        '''
        form overide to set user who uploaded image
        '''
        form.instance.profile = self.request.user
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    '''
    Class based view for updating new image
    '''
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        '''
        form overide to set user who uploaded image
        '''
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        Function run by userpassestestmixin to check if user passes test to be able to update image
        '''
        image = self.get_object()
        if self.request.user == image.profile:
            return True
        return False

class ImageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    '''
    class based view to delete image object
    '''
    model = Image
    success_url = '/'

    def test_func(self):
        '''
        Function run by userpassestestmixin to check if user passes test to be able to delete image
        '''
        image = self.get_object()
        if self.request.user == image.profile:
            return True
        return False