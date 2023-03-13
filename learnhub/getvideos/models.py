from django.db import models


class GetVideos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    thumbnail = models.URLField()

    def __str__(self):
        return self.title
    