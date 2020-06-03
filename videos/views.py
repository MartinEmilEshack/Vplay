from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http.response import HttpResponse

from .models import Video

class VideoDetailView(DetailView):
	model = Video
	template_name = "video.html"
	
	def get_object(self):
		probe_hash = self.kwargs.get('vid_hash')
		# return get_object_or_404(Video, probe_hash=probe_hash)
		obj = get_object_or_404(Video, id=probe_hash)
		return obj