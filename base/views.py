from django.shortcuts import render
from .models import Gallery, Album

# Create your views here.
def index(request):
    albums = Album.objects.all()
    photos = Gallery.objects.all()
    context = {
        'albums':albums,
        'photos':photos,
    }
    return render(request, 'index.html',context)