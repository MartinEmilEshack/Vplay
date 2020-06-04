from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.http.response import HttpResponse

from .models import Video

class VideoListView(ListView):
	model = Video
	template_name = "video_list.html"

	def get_queryset(self):
		if self.request.GET.get("id"):
			_id = self.request.GET.get("id")
			return Video.objects.filter(id__gt=_id)
		else:
			return super().get_queryset()

class VideoDetailView(DetailView):
	model = Video
	template_name = "display.html"	
	
	def get_object(self):
		probe_hash = self.kwargs.get('vid_hash')
		# return get_object_or_404(Video, probe_hash=probe_hash)
		obj = get_object_or_404(Video, id=probe_hash)
		return obj

	def get(self, request, vid_hash = None, *args, **kwargs):
		obj = get_object_or_404(Video, id=vid_hash)
		videos = Video.objects.all()
		return render(request, self.template_name, {'object': obj, 'object_list': videos})
