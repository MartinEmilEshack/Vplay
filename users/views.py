from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from users import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignUpCreateView(CreateView):
    model = User
    template_name = "signup.html"
    fields = ['name', 'pw',]

def signupPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}            
    return render(request, 'hi.html',context)
    
class LogInCreateView(CreateView):
    model = User
    template_name = "login.html" 
    fields = ['name', 'pw',]
