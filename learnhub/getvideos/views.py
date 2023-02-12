from django.shortcuts import render
from .models import GetVideos
from dotenv import load_dotenv
import os
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from pytube import YouTube
import requests
from django.contrib import messages
from urllib.parse import quote
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


def base(request):
    return render(request, 'base/base.html')

# GET YOUTUBE TUTORIALS FROM YOUTUBE


@login_required
def get_videos(request):
    query = request.GET.get('q', '')
    # keywords = ['Django', 'Django web development']
    # query += " ".join(keywords)
    if not query:
        return render(request, 'getvideos/video_list.html')

    api_key = 'AIzaSyD8PA1Zwa1va-80_qi-DMIMNEE3V2YNHLQ'
    # api_key = os.getenv('API_KEY')
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&videoDefinition=any&maxResults=30&key={api_key}'
    response = requests.get(url)
    videos_data = response.json()['items']
    videos = []

    if not videos_data:
        messages.info(request, "no result found")

    # save the information in the database
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


# PYTUBE TO DOWNLOAD VIDEOS
@login_required
def download_video(request, video_id):
    url = f'https://www.youtube.com/watch?v={video_id}'
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, resolution='480p', file_extension='mp4')
    # stream = yt.streams.order_by('resolution')
    # stream = yt.streams.desc()
    stream = yt.streams.first()
    # encode_title= quote(title)
    download_name = 'video'
    stream.download()
    # file = open(download_name, 'rb')
    # response = FileResponse(file, content_type='application/force-download')
    # response['Content-Disposition'] = f'attachment; filename={download_name}'
    # return response


#  user = request.user.userprofile
#     url = f'https://www.youtube.com/watch?v={video_id}'
#     yt = YouTube(url)

#     quality = user.vid_quality

#     stream = yt.streams.get_by_resolution('360p')
#     if stream is None:
#         stream = yt.streams.first()
#     download_name = 'video'
#     stream.download('/downloads')
#     file = open(download_name, 'rb')
#     response = FileResponse(file, content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="{download_name}.mp4"'
#     return response
# def download_video(request, video_id):
#     # video = GetVideos.objects.get(video_id=video_id)
#     video_id =request.GET.get('video_data', None)
#     url = video_.url
#     yt = YouTube(url)
#     stream = yt.streams.first()
#     file_name = f"{video.title}.mp4"
#     file_path = os.path.join(os.path.dirname(
#         os.path.abspath(__file__)), file_name)
#     stream.download(file_path)
#     file = open(file_path, 'rb')
#     response = FileResponse(file, content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="{file_name}"'
#     return response

# GET https: // youtube.googleapis.com/youtube/v3/search?part = snippet &maxResults = 25&q = surfing&key = [YOUR_API_KEY] HTTP/1.1
