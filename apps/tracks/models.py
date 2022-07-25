from django.db import models
from apps.albums.models import Albums


class Tracks(models.Model):
    album = models.ForeignKey(
        to=Albums,
        related_name='album',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=35)
    image = models.ImageField(upload_to='albums/')
    plays_count = models.PositiveBigIntegerField(default=0)
    file = models.FileField(upload_to='music_files/')

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

