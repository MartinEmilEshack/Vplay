from django import forms

from .models import User

class LogInForm(forms.ModelForm):

    pw = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = [
            'name',
            'pw',
        ]

class SignUpForm(forms.ModelForm):

    pw = forms.CharField(widget=forms.PasswordInput())
    pwc = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'name',
            'pw',
        ]
    
