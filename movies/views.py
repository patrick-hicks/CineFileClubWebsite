from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import MovieForm

# Create your views here.

def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)

def user_ratings(request, username):
    try:
      user = User.objects.get(username=username)
      context = {
          'ratings':user.ratings.all(),
          'user': request.user
      }
      return render(request, 'user_ratings.html', context)
    except User.DoesNotExist:
      context = {
          'user': request.user,
          'error_msg': f'The requested user "{username}" does not exist in the system.'
      }
      return render(request, 'error.html', context)

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

