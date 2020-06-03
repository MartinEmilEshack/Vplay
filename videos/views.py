from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http.response import HttpResponse

from .models import Video
from vplay_web.settings import MEDIA_URL, MEDIA_ROOT


class VideoDetailView(DetailView):
	model = Video
	template_name = "video.html"
	
	def get_object(self):
		probe_hash = self.kwargs.get('vid_hash')
		# return get_object_or_404(Video, probe_hash=probe_hash)
		obj = get_object_or_404(Video, id=probe_hash)
		print(obj.video_file.name)
		return obj


def display_video(request,vid_hash=None):
    if vid_hash is None:
        return HttpResponse("No Video")

    try:
        video_object = get_object_or_404(Video, id=vid_hash)
    except Video.DoesNotExist:
        return HttpResponse("Id doesn't exists.")

    file_name = video_object.video_file.name
    #getting full url - 
    video_url = MEDIA_URL+ file_name

    return render(request, "video.html", {"url":video_url})

# def display_video(request,vid_hash=None):
#    return render(request, "video.html", {})
