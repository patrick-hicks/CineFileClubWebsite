from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.

def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)

def add_movie(request):
    submitted = False
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_movie?submitted=True')
    else:
        form = MovieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_movie.html', {'form': form, 'submitted': submitted})

