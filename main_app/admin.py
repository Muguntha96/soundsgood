from django.contrib import admin

from main_app.models import Playlist,Song

# Register your models here.
admin.site.register(Playlist)
admin.site.register(Song)