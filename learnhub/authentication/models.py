from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    def __str__(self):
        return self.username


VIDEO_QUALITY = (
    ('240p', '240p'),
    ('360p', '360p'),
    ('480p', '480p'),
    ('720p', '720p'),
    ('1080p', '1080p'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    vid_quality = models.CharField(
        choices=VIDEO_QUALITY, default='240p', max_length=5)
