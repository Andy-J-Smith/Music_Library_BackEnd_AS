from django.urls import path
from . import views

urlpatterns = [
path('', views.songs_list),
path('api/music/songs/<int:pk>/', views.songs_list),
]

