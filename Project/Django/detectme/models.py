from django.db import models
import datetime
# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)


class SongUrl(models.Model):
    id_index = models.TextField(primary_key=True, null=False, blank=True)  # Field name made lowercase.
    tags = models.TextField(null=False, blank=True)
    issue_date = models.TextField(null=False, blank=True)
    album_name = models.TextField(null=False, blank=True)
    artist_name_basket = models.TextField(null=False, blank=True)
    song_name = models.TextField(null=False, blank=True)
    song_url = models.TextField(null=False, blank=True)

    class Meta:
        managed = False
        db_table = 'song'

