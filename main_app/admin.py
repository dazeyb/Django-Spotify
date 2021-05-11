from django.contrib import admin
# this will import the Artist Model
from .models import Artist, Song


# Register your models here.

admin.site.register(Artist)
admin.site.register(Song)
