from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField

# Create your models here.


class Artist(Model):

    name = CharField(max_length=100)
    img = CharField(max_length=120)
    bio = TextField(max_length=500)
    verified_artist = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
