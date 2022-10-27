from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    likes = models.CharField(max_length=30)
    artiste_id = models.CharField(max_length=30)
   
class Lyric(models.Model):
    content = models.CharField(max_length=30)
    song_id = models.CharField(max_length=30)

