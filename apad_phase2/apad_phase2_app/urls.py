from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^email$', views.emailForm),
    url(r'^venueFormPath$', views.venueForm),
    url(r'^insertVenuePath$', views.insertVenue),
    url(r'^CreateJoinPath$', views.createOrJoin),
    url(r'^CreateEventPath$', views.createEvent),
    url(r'^InsertEventPath$', views.insertNewEvent),
]