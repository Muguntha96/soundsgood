from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView, DetailView
from .models import Playlist,Song

from main_app.models import Playlist

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def playlist_index(request):
  playlists=Playlist.objects.all()
  return render(request,'playlists/index.html',{'playlists':playlists})

def playlist_detail(request,playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request,'playlists/detail.html',{'playlist':playlist})

def playlist_delete(request,playlist_id):
  Playlist.objects.get(id=playlist_id).delete()
  return redirect('playlist-index')
class PlaylistCreate(CreateView):
  model = Playlist
  fields = '__all__'
  success_url = '/playlists/' 
  
class PlaylistUpdate(UpdateView):
  model=Playlist
  fields=['title','genre','description']
  
class SongCreate(CreateView):
  model = Song
  fields = '__all__'
  success_url = '/songs/'

class SongList(ListView):
  model = Song
  