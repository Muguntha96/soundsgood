from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('playlists/',views.playlist_index,name='playlist-index'),
    path('playlists/<int:playlist_id>',views.playlist_detail,name='playlist-detail'),
    path('playlists/create/',views.PlaylistCreate.as_view(),name='playlist-create')
]
