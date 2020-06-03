from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = [
			"video_file",
			"name",
			"description",
			"tags",
		]

# description = forms.CharField(
# 		widget= forms.Textarea(
# 			attrs={
# 				'placeholder': 'Add description..',
# 				'rows': 10,
# 				'cols': 30
# 		})
# 	)
# 	tags = forms.CharField(
# 		widget= forms.Textarea(
# 			attrs={
# 				'placeholder': 'music-minecraft-pewdiepie-..',
# 				'row': 10,
# 				'cols': 30
# 		})
# 	)
# 	duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M:%S'))