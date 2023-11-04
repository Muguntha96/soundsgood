from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Playlist

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

class PlaylistCreate(CreateView):
  model = Playlist
  fields = '__all__'