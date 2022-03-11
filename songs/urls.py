from django.urls import path
from . import views


urlpatterns = [
    path('', views.songs_list),
    path('<int:pk>/', views.songs_detail),
    path('<int:pk>/', views.like_song),
]

