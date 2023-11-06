import mimetypes
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView, DetailView
from .models import Playlist,Song
from .forms import SongSearchForm, UploadSongandImageForm,UploadImagePlaylistForm
from main_app.models import Playlist,Song
from django.contrib.auth.views import LoginView

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request,'about.html')

def playlist_index(request):
  playlists=Playlist.objects.all()
  return render(request,'playlists/index.html',{'playlists':playlists})

def playlist_detail(request,playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  songs=None
  if request.method == "GET":
    form = SongSearchForm(request.GET)
    query_name = None
    if form.is_valid():
      query_name = form.cleaned_data.get('query_name')
      if query_name:
        songs = Song.objects.all()
        songs = songs.filter(
          Q(title__icontains=query_name)|Q(composer__icontains=query_name)|Q(genre__icontains=query_name)
          )
      else:
        songs=[]
    context = {
    'playlist': playlist,
    'songs': songs,
    'form': form,
    'query_name': query_name,
    }
  return render(request,'playlists/detail.html',context)

def playlist_delete(request,playlist_id):
  Playlist.objects.get(id=playlist_id).delete()
  return redirect('playlist-index')
class PlaylistCreate(CreateView):
  model = Playlist
  fields = ['title','description','genre','playlist_image']
  playlist_form=UploadImagePlaylistForm
  success_url = '/playlists/' 
  
class PlaylistUpdate(UpdateView):
  model=Playlist
  fields=['title','genre','description']
  
class SongCreate(CreateView):
  model = Song
  fields = '__all__'
  form=UploadSongandImageForm
  success_url = '/songs/'

class SongList(ListView):
  model = Song
  def play_song(self,song_id):
    song=Song.objects.get(id=song_id)
    audio=song.audio_file.path
    content_type, _ = mimetypes.guess_type(audio)
    return FileResponse(open(audio, 'rb'), content_type=content_type)
class SongDetail(DetailView):
  model = Song

class SongUpdate(UpdateView):
  model = Song
  fields =['title','genre']

def song_delete(request,song_id):
  Song.objects.get(id=song_id).delete()
  return redirect('song-index')

def assoc_song(request,playlist_id,song_id):
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect('playlist-detail',playlist_id=playlist_id)

# def play_song(request,playlist_id,song_id):
  