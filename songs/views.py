from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

from songs import serializers

@api_view(['GET'])
def songs_list(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def songs_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    serializer = SongSerializer(song)
    return Response(serializer.data, status=status.HTTP_200_OK)