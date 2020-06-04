"""vplay_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view, display_view, login_view, signup_view #aniki you suck
from users.views import LogInCreateView, SignUpCreateView #martin was here 8^)
from videos.views import VideoDetailView, VideoListView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', display_view, name = 'display'),
    path('', home_view, name='home'),
    path('login/', LogInCreateView.as_view() , name = 'login'),
    path('signup/', SignUpCreateView.as_view(), name = 'signup'),
    path('videos/<int:id>/', VideoListView.as_view()),
    path('video/<int:vid_hash>/', VideoDetailView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()