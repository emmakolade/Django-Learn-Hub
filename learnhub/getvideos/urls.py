from django.urls.conf import path
from . import views

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.get_videos, name='video_list'),
    path('download/<str:video_id>/', views.download_video, name='download'),
    path('download_quality/<str:video_id>/',
         views.download_quality, name='download_quality'),

]
