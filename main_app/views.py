import mimetypes
from django.forms.models import BaseModelForm
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Playlist, Song
from .forms import SongSearchForm, UploadSongandImageForm, UploadImagePlaylistForm
from main_app.models import Playlist, Song
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def is_admin(user):
    return user.is_staff
class Home(LoginView):
    template_name = "home.html"

def about(request):
    return render(request, "about.html")

@login_required
def playlist_index(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, "playlists/index.html", {"playlists": playlists})

@login_required
def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = None
    if request.method == "GET":
        form = SongSearchForm(request.GET)
        query_name = None
        if form.is_valid():
            query_name = form.cleaned_data.get("query_name")
            if query_name:
                songs = Song.objects.all()
                songs = songs.filter(
                    Q(title__icontains=query_name)
                    | Q(composer__icontains=query_name)
                    | Q(genre__icontains=query_name)
                )
            else:
                songs = []
        context = {
            "playlist": playlist,
            "songs": songs,
            "form": form,
            "query_name": query_name,
        }
    return render(request, "playlists/detail.html", context)

@login_required
def playlist_delete(request, playlist_id):
    Playlist.objects.get(id=playlist_id).delete()
    return redirect("playlist-index")
class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ["title", "description", "genre", "playlist_image"]
    success_url = "/playlists/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ["title", "genre", "description"]
class SongCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Song
    fields = "__all__"
    form = UploadSongandImageForm
    success_url = "/songs/"

    def get_permission_required(self):
        return ["main_app.add_song"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class SongList(LoginRequiredMixin, ListView):
    model = Song
    def play_song(self, song_id):
        song = Song.objects.get(id=song_id)
        audio = song.audio_file.path
        content_type, _ = mimetypes.guess_type(audio)
        return FileResponse(open(audio, "rb"), content_type=content_type)

class SongDetail(LoginRequiredMixin, DetailView):
    model = Song
class SongUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Song
    fields = ["title", "genre"]
    permission_required = "main_app.edit_song"

@login_required
@user_passes_test(is_admin)
def song_delete(request, song_id):
    Song.objects.get(id=song_id).delete()
    return redirect("song-index")

@login_required
def assoc_song(request, playlist_id, song_id):
    Playlist.objects.get(id=playlist_id).songs.add(song_id)
    return redirect("playlist-detail", playlist_id=playlist_id)

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("song-index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
