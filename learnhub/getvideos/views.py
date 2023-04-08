from django.shortcuts import render
from .models import GetVideos
from dotenv import load_dotenv
import os
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from pytube import YouTube
import requests
from django.contrib import messages

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Un-Authenticated Users will be redirected here
# def base(request):
#     return render(request, 'base/base.html')


# GET YOUTUBE VIDOES FROM YOUTUBE API

def get_videos(request):
    query = request.GET.get('q', '')
    # keywords = ['Django', 'Django web development']
    # query += " ".join(keywords)
    if not query:
        return render(request, 'getvideos/video_list.html')

    api_key = os.getenv('API_KEY')
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&videoDefinition=any&maxResults=30&key={api_key}'
    response = requests.get(url)
    videos_data = response.json()['items']
    videos = []

    if not videos_data:
        messages.info(request, "no result found")

    for video in videos_data:
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        thumbnail = video['snippet']['thumbnails']['high']['url']
        url = f'https://www.youtube.com/watch?v={video_id}'
        videos.append({
            'title': title,
            'description': description,
            'url': url,
            'thumbnail': thumbnail,
            'video_id': video_id
        })
    return render(request, 'getvideos/video_list.html', {'videos': videos})


def download_quality(request, video_id):
    url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    video_qualities = [s.resolution for s in stream]
    context = {
        'video_id': video_id,
        'video_title': yt.title,
        'video_qualities': video_qualities
    }
    return render(request, 'getvideos/video_list.html', context)


def download_video(request, video_id, quality):
    url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(url)
    stream = yt.streams.filter(
        progressive=True, file_extension='mp4', resolution=quality).first()
    video_file = stream.download()
    response = FileResponse(open(video_file, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{yt.title} ({quality}).mp4"'
    return response


# PYTUBE TO DOWNLOAD VIDEOS
# def download_video(request, video_id):
#     url = f'https://www.youtube.com/watch?v={video_id}'
#     yt = YouTube(url)
#     stream = yt.streams.filter(
#         progressive=True, file_extension='mp4').first()
#     video_file = stream.download()
#     response = FileResponse(open(video_file, 'rb'))
#     response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
#     return response
# GET https: // youtube.googleapis.com/youtube/v3/search?part = snippet &maxResults = 25&q = surfing&key = [YOUR_API_KEY] HTTP/1.1
