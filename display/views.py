from django.shortcuts import render

# Create your views here.
def display_view(request):
	return render(request, 'home/display.html', {})