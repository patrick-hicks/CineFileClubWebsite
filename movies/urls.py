from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),

    path('ratings/<str:username>/', views.user_ratings, name = "user-ratings"),
]