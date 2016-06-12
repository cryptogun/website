from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
#ALBUM red has primary key 1
class Album(models.Model):
    artist = models.CharField(max_length=250) #will migrate as a name of column
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100) #classic, country music...
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + " - " + self.artist

class Song(models.Model):
    #belongs to one album, foreignkey relates to primary key e.g 1.
    # cascade: delete album, all songs in it will be deleted.
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10) #mp3, wav ...
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title



