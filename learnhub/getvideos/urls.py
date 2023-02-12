from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('video_list/', views.get_videos, name='video_list'),
    path('download/<str:video_id>/', views.download_video, name='download'),
]
