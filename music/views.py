from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import Album
from django.http import Http404

# Create your views here.
#music index page
def index(request):
    all_albums = Album.objects.all()
    #context = {'all_albums': all_albums }
    return render(request, 'music/index.html', {'all_albums': all_albums })

#single music page /music/1/
def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album not found")
    return render(request, 'music/detail.html', {'album': album})
