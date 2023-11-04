from django.shortcuts import render
from django.http import HttpResponse

class Playlist:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, description, genre):
    self.title = title
    self.description = description
    self.genre = genre
  

playlists = [
  Playlist('Lolo', 'tabby', 'Kinda rude.'),
  Playlist('Sachi', 'tortoiseshell', 'Looks like a turtle.'),
  Playlist('Fancy', 'bombay', 'Happy fluff ball.'),
  Playlist('Bonk', 'selkirk rex', 'Meows loudly.')
]
    

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def playlist_index(request):
  return render(request,'playlists/index.html',{'playlists':playlists})