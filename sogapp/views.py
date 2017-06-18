from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserContactForm
from .models import ArtistInfo

# Create your views here.

app_name = 'sogapp'
def index(request):
	return render(request, "sogapp/index.html")


def recording_artist_view(request):
	artist_info = ArtistInfo.objects.all()
	return render(request, "sogapp/recording_artist.html", {"artist_info": artist_info})


def music_release(request):
	return render(request, "sogapp/music_release.html")

def upcommingshows(request):

	return render(request, "sogapp/shows.html")

def contact_view(request):
    if request.method == "POST":
        print("Hello")
        form = UserContactForm(request.POST or None)
        if form.is_valid():
            form_data = form.save(commit=False)
            print(form_data.first_name)
            form.save()
            return redirect('sogapp:thanks_view')
    else:
        form = UserContactForm()
        return render(request, 'sogapp/contact.html', {'form':form})

def thanks_view(request):
    return render(request, "sogapp/thanks.html")


def artist_details(request, pk):
	artist_info = get_object_or_404(ArtistInfo, pk=pk);
	return render(request, 'sogapp/artist_detail_info.html', {"artist_info":artist_info})
