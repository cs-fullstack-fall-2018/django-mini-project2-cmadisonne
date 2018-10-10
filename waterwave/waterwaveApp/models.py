from django.db import models


class Waterwave(models.Model):
    songName = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.songName