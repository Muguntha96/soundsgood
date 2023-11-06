from django.db import models
from django.urls import reverse
from django.utils import timezone

GENRE=(
    ('Pop','Pop'),
    ('Jazz','Jazz'),
    ('Melody', 'Melody'),
    ('Workout', 'Workout'),
    ('Travel', 'Travel'),
    ('Night Times', 'Night Times'),
)
# Create your models here.

class Song(models.Model):
  title=models.CharField(max_length=50)
  genre=models.CharField(
    max_length=50,
    choices=GENRE,
    default=GENRE[0][0]
  )
  composer=models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/')
  audio_file = models.FileField(upload_to='songs/')
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("song-detail", kwargs={"pk": self.id})
  
  

  
class Playlist(models.Model):
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=300)
  genre=models.CharField(
    max_length=100,
    choices=GENRE,
    default=GENRE[0][0]
  )
  playlist_image=models.ImageField(upload_to='images/')
  songs = models.ManyToManyField(Song)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("playlist-detail", kwargs={"playlist_id": self.id})
  