from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('ratings/<str:username>/', views.user_ratings, name = "user-ratings"),
    path('compare_users/<str:username1>/<str:username2>/', views.user_compare, name = "user-ratings"),
    path('add_movie/', views.add_movie, name = "add-movie")
]