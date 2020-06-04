import os
import hashlib
import json

from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models

import ffmpeg

from vplay_web.settings import BASE_DIR,MEDIA_ROOT

class VideoSystemStorage(FileSystemStorage):
	def get_available_name(self, name, max_length=None):
		if max_length and len(name) > max_length:
			raise(Exception("Name's length is greater than max_length"))
		return name

	def _save(self, name, content):
		if self.exists(name):
			return name
		return super(VideoSystemStorage, self)._save(name, content)

class Video(models.Model):
	video_file 		= models.FileField(storage=VideoSystemStorage())
	name 				= models.CharField(max_length=50)
	description 	= models.TextField(blank=True, null=True)
	tags 				= models.TextField(blank=True, null=True) # music-bla-bla-
	
	# non shown fields
	duration 		= models.TimeField(editable=False, null=False)
	probe_hash 		= models.CharField(editable=False, max_length=100, unique=True, null=False)
	thumbnail_path = models.CharField(editable=False, max_length=50, null=False)

	print('vsrc')

	def clean(self):
		video_path = self.video_file.name.replace(' ','_')
		video_path = os.path.join(BASE_DIR,MEDIA_ROOT,video_path)

		try:
			video_probe = ffmpeg.probe(video_path)
		except ffmpeg.Error as e:
			return super().clean()
		except FileNotFoundError as e:
			print(e)
			return super().clean()

		hashed_probe = hashlib.md5(json.dumps(video_probe).encode('utf-8')).hexdigest()

		if self.probe_hash == hashed_probe or not self.probe_hash:
			raise ValidationError("File already exist!")
		return super().clean()
	
	def __str__(self):
		return self.name
	
	# def save(self, *args, **kwargs):
	# 	if not self.pk:  # file is new
	# 		md5 = hashlib.md5()
	# 		for chunk in self.orig_file.chunks():
	# 				md5.update(chunk)
	# 		self.probe_hash = md5.hexdigest()
	# 	super(Video, self).save(*args, **kwargs)