from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# auth imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# import models
from .models import Artist, Song, Playlist

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')
class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")
        if name_query != None:
            context["artists"] = Artist.objects.filter(
                name__icontains=name_query, user=self.request.user)
            context["header"] = f"Searching for {name_query}"
        else:
            context["artists"] = Artist.objects.filter(user=self.request.user)
            context["header"] = "Trending Artists"
        return context


@method_decorator(login_required, name='dispatch')
class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})


class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"

    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"


class SongCreate(View):
    # just to show you can do whatever request you wish
    def get(self, request, pk):
        # this is the same as template_name=home.html
        return render(request, "home.html")

    def post(self, request, pk):
        title_data = request.POST.get("title")
        length_data = request.POST.get("length")
        # SELECT * FROM main_app_artist WHERE id=1;
        artist_found = Artist.objects.get(pk=pk)
        Song.objects.create(
            title=title_data, length=length_data, artist=artist_found)
        return redirect('artist_detail', pk=pk)


class PlaylistSongAssoc(View):

    def get(self, request, pk, song_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Playlist.objects.get(pk=pk).songs.remove(song_pk)
        if assoc == "add":
            Playlist.objects.get(pk=pk).songs.add(song_pk)
        return redirect('home')


class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            return redirect("signup")
