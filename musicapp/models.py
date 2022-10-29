from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()


class Song (models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric (models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)