from django.shortcuts import render

from videos.models import Video

# Create your views here.
def home_view(request):
	videos = Video.objects.all()
	return render(request, 'home.html', {'object_list':videos})

def display_view(request):
	return render(request, 'display.html', {})

def login_view(request):
	return render(request, 'login.html', {})

def signup_view(request):
	return render(request, 'signup.html', {})