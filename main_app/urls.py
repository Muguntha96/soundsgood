from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('playlists/',views.playlist_index,name='playlist-index'),
    path('playlists/<int:playlist_id>/',views.playlist_detail,name='playlist-detail'),
    path('playlists/create/',views.PlaylistCreate.as_view(),name='playlist-create'),
    path('playlists/<int:pk>/update/',views.PlaylistUpdate.as_view(),name='playlist-update'),
    path('playlists/<int:playlist_id>/delete/',views.playlist_delete,name='playlist-delete'),
    path('songs/create',views.SongCreate.as_view(),name='song-create'),
    path('songs/<int:pk>/',views.SongDetail.as_view(),name='song-detail'),
    path('songs/', views.SongList.as_view(), name='song-index'),
    path('songs/play/<int:song_id>',views.SongList.as_view(),name='play-song'),
    path('songs/<int:pk>/update/',views.SongUpdate.as_view(),name='song-update'),
    path('songs/<int:song_id>/delete/',views.song_delete,name='song-delete'),
    path('playlists/<int:playlist_id>/assoc-song/<int:song_id>/',views.assoc_song,name='assoc-song'),
    # path('playlists/<int:playlist_id>/play-song/<int:song_id>/',views.play_song,name='play_song'),
]
