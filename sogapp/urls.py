from django.conf.urls import url
from . import views

app_name = "sogapp"
urlpatterns =[
	# url(r'^about', views.about, name="about"),
	url(r'^recording/artists/$', views.recording_artist_view, name="recording_artist_view"),
	url(r'^music/release/$', views.music_release, name="music_release"),
	url(r'^music/shows/$', views.upcommingshows, name="upcommingshows"),
	url(r'^music/contact/page/$', views.contact_view, name="contact_view"),
	url(r'^music/thanks/page/$', views.thanks_view, name="thanks_view"),

]