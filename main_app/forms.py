from django import forms
from .models import Song
class SongSearchForm(forms.Form):
  query_name = forms.CharField(max_length=100, required=False, label='Search for a Song')

class UploadSongForm(forms.ModelForm):
  class Meta:
    model = Song
    fields=['title','genre','composer','audio_file']