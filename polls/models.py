from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Toplist(models.Model):
    toplist_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.toplist_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Song(models.Model):
    toplist = models.ForeignKey(Toplist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.song_title
