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
from django.contrib.auth import views as auth_views
from psevents import views as main_views
from django.conf import settings


urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('psevents.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', main_views.signup, name='signup'),
    url(r'^$', main_views.home, name='home'),
    path('list/', main_views.venue_list_view, name='venue-list'),
    path('create/', main_views.venue_create_view, name='venue-create'),
    path('<int:id>/update/', main_views.venue_update_view, name='venue-update'),
    path('<int:id>/delete/', main_views.venue_delete_view, name='venue-delete'),    
    path('event-cat-create/', main_views.event_cat_create_view, name='event-cat'),
    path('sports-create/', main_views.sport_create_view, name='sports-create'),
    path('event-create/', main_views.event_create_view, name='event-create'),
    path('slots/', main_views.slot_view, name='find-slot'),
    path('venues/', main_views.venue_avail_view, name='find-venue'),
    path('event-delete/', main_views.event_delete_view, name='delete-event'),
    path('events/', main_views.event_view, name='events')


]


if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)