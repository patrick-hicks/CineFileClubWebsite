from django.shortcuts import render, redirect
from .models import *
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