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
  title = models.CharField(max_length=100)
  genre=models.CharField(
    max_length=100,
    choices=GENRE,
    default=GENRE[0][0]
  )
  released_year=models.PositiveIntegerField(
    verbose_name="Released Year",
    default={'min_value':1900,'max_value':2099},
    blank=True,
    null=True,
    help_text="The year in which it was released."
  )
  
class Playlist(models.Model):
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=300)
  genre=models.CharField(
    max_length=100,
    choices=GENRE,
    default=GENRE[0][0]
  )
  songs = models.ManyToManyField(Song)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse("playlist-detail", kwargs={"playlist_id": self.id})
  