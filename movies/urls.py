from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('add_movie/', views.add_movie, name = "add-movie")
]