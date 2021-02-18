from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .serializers import CreateArtistSerializer, TestCreateSerializer
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import CreateArtistForm
from .models import CreateArtist

@api_view(['POST'])
def createArtist(request):
    serializer = CreateArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(serializer.data)

@api_view(['GET'])
def showArtist(request):
    artist = CreateArtist.objects.all()
    serializer = CreateArtistSerializer(artist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    form = CreateArtistForm()
    if request.method == 'POST':
        form = CreateArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('bad')
    return render(request, 'form.html', {"form": form})

def success(request):
    return HttpResponse('done uploaded')