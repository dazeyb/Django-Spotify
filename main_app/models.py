from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ManyToManyField

# import user model from built in auth
from django.contrib.auth.models import User

import time
from time import strftime
# Create your models here.


class Artist(Model):

    name = CharField(max_length=100)
    img = CharField(max_length=500)
    bio = TextField(max_length=500)
    verified_artist = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    # connection to user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# artist.songs => all songs by the given artist
# without related name
# artist.song_set


class Song(Model):

    title = CharField(max_length=150)
    length = models.IntegerField(default=0)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return f"{self.title} BY: {self.artist.name}"

    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))


class Playlist(Model):

    title = CharField(max_length=150)
    # to create a many to many relationship aka a join table
    songs = ManyToManyField(Song)

    def __str__(self):
        return self.title
