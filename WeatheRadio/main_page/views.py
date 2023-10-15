from django.shortcuts import render
from django.http import HttpResponse
from . import complete_Implimentation
import time

def index(request):
    song = complete_Implimentation.getSong()
    return render(request, 'index.html', context={"song_link": "https://open.spotify.com/embed/track/"+song+"?utm_source=generator"})

