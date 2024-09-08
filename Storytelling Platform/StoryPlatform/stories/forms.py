from django import forms
from .models import Story, StoryChapter
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'autofocus': True
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story 
        fields = ['title', 'description']


class StoryChapterForm(forms.ModelForm):
    class Meta:
        model = StoryChapter
        fields = ['content', 'choice_text', 'parent_node']