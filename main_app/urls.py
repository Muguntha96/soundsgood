from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('playlists/',views.playlist_index,name='playlist-index'),
    path('playlits/<int:playlist_id>/',views.playlist_detail,name='playlist-detail'),
]
