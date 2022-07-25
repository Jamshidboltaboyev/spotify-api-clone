from django.urls import path

from .views import (
    get_albums,
    get_album_by_id,
    get_album_tracks
)


urlpatterns = [
    path("albums/", get_albums),
    path("albums/<int:id>/", get_album_by_id),
    path("albums/<int:id>/tracks/", get_album_tracks),
]
