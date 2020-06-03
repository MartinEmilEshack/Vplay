import os
import hashlib
import json

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import admin

import ffmpeg

from .models import Video
from vplay_web.settings import BASE_DIR,MEDIA_ROOT

def get_thumbnail(video, frame_num):
	out, err = (
		ffmpeg
		.input(video)
		.filter('select', 'gte(n,{})'.format(frame_num))
		.output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
		.run(capture_stdout=True)
	)
	return out

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		try:
			video_path = obj.video_file.name.replace(' ','_')
			thumbnail_path = video_path.replace('.mp4','.jpeg')

			video_path = os.path.join(BASE_DIR,MEDIA_ROOT,'@'+video_path)
			thumbnail_path = os.path.join(BASE_DIR,MEDIA_ROOT,thumbnail_path)

			video = request.FILES['video_file']
			video_path = default_storage.save(video_path, ContentFile(video.read()))

			thumbnail = get_thumbnail(video_path,1)
			thumbnail_path = default_storage.save(thumbnail_path, ContentFile(thumbnail))

			video_probe = ffmpeg.probe(video_path)
			obj.probe_hash = hashlib.md5(json.dumps(video_probe).encode('utf-8')).hexdigest()

			sec = float(video_probe['format']['duration'])
			mint, sec = divmod(sec, 60)
			hr, mint = divmod(mint, 60)
			duration = '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(hr,mint,sec)

			os.remove(video_path)

			obj.duration = duration
			obj.thumbnail_path = thumbnail_path

			super().save_model(request, obj, form, change)

		except ffmpeg.Error as e:
			print(e.stderr)



