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
class Playlist(models.Model):
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=300)
  genre=models.CharField(
    max_length=100,
    choices=GENRE,
    default=GENRE[0][0]
  )

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("playlist-detail", kwargs={"playlist_id": self.id})
  