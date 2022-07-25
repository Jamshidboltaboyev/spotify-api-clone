import os

from django.db import models


class Genres(models.Model):
    image = models.ImageField(upload_to='genres')
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        print(self.image.url)
        return super(Genres, self).delete()

        