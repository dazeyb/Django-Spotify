from django.urls import path
from . import views

from .views import Home, About, ArtistList, ArtistCreate, ArtistDetail, ArtistUpdate, ArtistDelete, SongCreate, PlaylistSongAssoc, Signup

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('artists/', ArtistList.as_view(), name="artist_list"),
    path('artists/new/', ArtistCreate.as_view(), name="artist_create"),
    path('artists/<int:pk>/', ArtistDetail.as_view(), name="artist_detail"),
    path('artists/<int:pk>/update/',
         ArtistUpdate.as_view(), name="artist_update"),
    path('artists/<int:pk>/delete/',
         ArtistDelete.as_view(), name="artist_delete"),
    path('artists/<int:pk>/songs/new/',
         SongCreate.as_view(), name="song_create"),
    path('playlists/<int:pk>/songs/<int:song_pk>/',
         PlaylistSongAssoc.as_view(), name="playlist_song_assoc"),
    path('accounts/signup/', Signup.as_view(), name="signup")
]
