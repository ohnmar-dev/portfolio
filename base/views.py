from django.shortcuts import render
from .models import Gallery, Album, Category, Blog

# Create your views here.
def index(request):
    albums = Album.objects.all()
    photos = Gallery.objects.all()
    blogs = Blog.objects.all()
    context = {
        'albums':albums,
        'photos':photos,
        'blogs':blogs,
    }
    return render(request, 'index.html',context)