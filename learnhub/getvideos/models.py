from django.db import models


class GetVideos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    thumbnail = models.URLField()
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class DownloadVideo(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     url = models.URLField()
#     thumbnail = models.URLField()
#     video_id = models.CharField(max_length=100)

#     def __str__(self):
#         return self.d
