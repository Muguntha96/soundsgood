from django import forms
from .models import  Song,Playlist
class SongSearchForm(forms.Form):
  query_name = forms.CharField(max_length=100, required=False, label='Search for a Song')

class UploadSongandImageForm(forms.ModelForm):
  class Meta:
    model = Song
    fields=['title','genre','composer','image','audio_file']

class UploadImagePlaylistForm(forms.ModelForm):
  class Meta:
    model=Playlist
    fields = ['title','description','genre','playlist_image']


      
