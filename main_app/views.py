from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView, DetailView
from .models import Playlist,Song
from .forms import SongSearchForm
from main_app.models import Playlist,Song

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
  songs=None
  if request.method == "GET":
    form = SongSearchForm(request.GET)
    query_name = None
    if form.is_valid():
      query_name = form.cleaned_data.get('query_name')
      if query_name:
        songs = Song.objects.all()
        songs = songs.filter(title__contains=query_name)
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
  fields = ['title','description','genre']
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

class SongDetail(DetailView):
  model = Song

class SongUpdate(UpdateView):
  model = Song
  fields =['title','genre']

def song_delete(request,song_id):
  Song.objects.get(id=song_id).delete()
  return redirect('song-index')

# def search_song(request):
#   if request.method == "POST":
#     query_name = request.POST.get('title',None)
#     if query_name:
#       results = Song.objects.filter(title__contains=query_name)
#       return render(request,'song_list.html',{"results":results})