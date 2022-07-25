from django.contrib.auth import get_user_model

from django.db import models

from apps.genres.models import Genres

artist = get_user_model()


class Albums(models.Model):

    name = models.CharField(max_length=64)
    release_date = models.DateField(auto_now_add=True)

    artists = models.ManyToManyField(artist, related_name='artist')
    genres = models.ManyToManyField(
        Genres,
        related_name='genre'
    )

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.name

    def url_source(self):
        return "http://localhost"
