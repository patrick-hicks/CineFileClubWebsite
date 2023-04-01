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
    

def user_compare(request, username1, username2):
    
    try:
      user1 = User.objects.get(username=username1)
      user2 = User.objects.get(username=username2)

      query = Movie.objects.raw(
         f"SELECT Movie.id, Movie.title as title, Ratings_user1.score as user1_score, Ratings_user2.score as user2_score FROM movies_movie as Movie JOIN movies_rating as Ratings_user1 ON Ratings_user1.movie_id = Movie.id AND Ratings_user1.user_id = {user1.id}\
          JOIN movies_rating as Ratings_user2 ON Ratings_user2.movie_id = Movie.id AND Ratings_user2.user_id = {user2.id}"
      )
    except User.DoesNotExist:
      context = {
          'user': request.user,
          'error_msg': f'One Or more users not found.'
      }
      return render(request, 'error.html', context)
    context = {
          'user': request.user,
          'user1':user1,
          'user2':user2,
          'movies': query
    }
    return render(request, 'user_compare.html', context)


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

