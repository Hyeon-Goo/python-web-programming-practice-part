from django.shortcuts import render
from django.views.generic import ListView, DetailView
from photo.models import Album, Photo


# Create your views here.
class AlbumLV(ListView):
    model = Album
    template_name = 'photo/album_list.html'


class AlbumDV(DetailView):
    model = Album
    template_name = 'photo/album_detail.html'


class PhotoDV(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'
