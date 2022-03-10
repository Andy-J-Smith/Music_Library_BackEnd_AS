from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

from songs import serializers

@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def songs_detail(request, pk):
    try:
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Song.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)