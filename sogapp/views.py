from django.shortcuts import render, redirect
from . forms import UserContactForm

# Create your views here.

app_name = 'sogapp'
def index(request):
	return render(request, "sogapp/index.html")


def recording_artist_view(request):
	return render(request, "sogapp/recording_artist.html")


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