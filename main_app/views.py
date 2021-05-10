from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse

# import models
from .models import Artist

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")
        if name_query != None:
            context["artists"] = Artist.objects.filter(
                name__icontains=name_query)
            context["header"] = f"Searching for {name_query}"
        else:
            context["artists"] = Artist.objects.all()
            context["header"] = "Trending Artists"
        return context


class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"

    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})


class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"

    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})
