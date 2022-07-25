from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Albums

from .serializers import AlbumSerializer


class AlbumsListAPIView(ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Albums.objects.all()


get_albums = AlbumsListAPIView.as_view()


def get_album_by_id(request):
    raise NotImplementedError()


def get_album_tracks(request):
    raise NotImplementedError()
