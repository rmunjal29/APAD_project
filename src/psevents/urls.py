"""phase2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

app_name = 'psevents'

urlpatterns = [
path('list/', venue_list_view, name='venue-list'),
path('venues/<int:id>/', venue_detail_view, name='venue-detail'),
path('sports/<int:id>/', sport_detail_view, name='sport-detail'),
path('venues/<int:id>/', venue_detail_view, name='venue-detail'),
path('ecv', EventCatView.as_view()),
path('ecv/<int:pk>/', EventCatDetail.as_view()),

path('vlv', VenueListView.as_view()),

path('sv/', SportView.as_view()),
path('sv/<int:pk>/', SportViewDetail.as_view()),

path('elv/', EventListView.as_view()),
path('elv/<int:pk>/', EventDetailView.as_view()),

path('jev', JoinedEventView.as_view()),

path('rest-auth/', include('rest_auth.urls')),

    
]

urlpatterns += staticfiles_urlpatterns()