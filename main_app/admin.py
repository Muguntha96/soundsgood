from django.contrib import admin

from main_app.models import Playlist,Song

# Register your models here.

class SongAdmin(admin.ModelAdmin):
  model = Song
  fields=['title','genre','composer','image','audio_file']
    
admin.site.register(Playlist)
admin.site.register(Song,SongAdmin)