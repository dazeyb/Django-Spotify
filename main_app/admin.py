from django.contrib import admin
# this will import the Artist Model
from .models import Artist


# Register your models here.

admin.site.register(Artist)
