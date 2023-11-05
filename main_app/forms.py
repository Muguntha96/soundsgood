from django import forms

class SongSearchForm(forms.Form):
  query_name = forms.CharField(max_length=100, required=False, label='Search for a Song')