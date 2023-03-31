from django import forms
from django.forms import ModelForm
from .models import Movie, Rating

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date')
        labels = {
            'title': '',
            'description': '',
            'release_date': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Movie Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter Description for Movie'}),
            'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }