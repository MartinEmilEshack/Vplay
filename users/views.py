from django.shortcuts import render

from django.views.generic import CreateView,DetailView

from .models import User

class SignUpCreateView(CreateView):
    model = User
    template_name = "signup.html"
    fields = ['name', 'pw',]

class LogInCreateView(CreateView):
    model = User
    template_name = "login.html" 
    fields = ['name', 'pw',]
