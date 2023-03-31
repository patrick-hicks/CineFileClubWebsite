from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)