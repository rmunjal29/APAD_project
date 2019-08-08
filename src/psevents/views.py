from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *


@login_required
def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

def signup(request):
	# print(request.user)
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.contact_number = form.cleaned_data.get('contact_number')
			user.profile.zip_code = form.cleaned_data.get('zip_code')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = UserForm()
	context = {
	'form': form
	}
	return render(request, 'signup.html', context)


def venue_create_view(request):
	if request.user.is_superuser:
		venue_form = VenueForm(request.POST or None)
		if venue_form.is_valid():
			venue_form.save()
			venue_form = VenueForm()
		context = {
		'form': venue_form
		}
		return render(request, "venues/venue-create.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not authorized to add a venue! (Admin only activity)')
		return redirect('home')


def venue_update_view(request, id=id):
	obj = get_object_or_404(add_venue, id=id)
	if request.user.is_superuser:
		update_form = VenueForm(request.POST or None, instance=obj)
		if update_form.is_valid():
			update_form.save()
		context = {
			'form': update_form,
			'key' : "update"
		}
		return render(request, "venues/venue-create.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not authorized to update a venue! (Admin only activity)')
		return redirect('home')

def venue_list_view(request):
	if request.user.is_authenticated:
		queryset = add_venue.objects.all() # list of objects
		context = {
			"object_list": queryset
		}
		return render(request, "venues/venue-list.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the list of venues')
		return redirect('login')

def venue_detail_view(request, id):
	if request.user.is_authenticated:
		obj = get_object_or_404(add_venue, id=id)
		context = {
			"object": obj
		}
		return render(request, "venues/venue-detail.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the details of venues')
		return redirect('login')

def venue_delete_view(request, id):
	if request.user.is_superuser:
		obj = get_object_or_404(add_venue, id=id)
		if request.method == "POST":
			obj.delete()
			return redirect('../../')
		context = {
			"object": obj
		}
		return render(request, "venues/venue-delete.html", context)
	else:
		messages.info(request, 'You are not authorized to delete a venue! (Admin only activity)')
		return redirect('home')


def event_cat_create_view(request):
	if request.user.is_superuser:
		event = event_cat(request.POST or None)
		if event.is_valid():
			event.save()
			event = event_cat()
		context = {
		'cat': event
		}
		return render(request, "events/event-cat-create.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not authorized to add a venue! (Admin only activity)')
		return redirect('home')


def sport_create_view(request):
	if request.user.is_superuser:
		event = sports(request.POST or None)
		if event.is_valid():
			event.save()
			event = sports()
		context = {
		'sports': event
		}
		return render(request, "events/sports-create.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not authorized to add a venue! (Admin only activity)')
		return redirect('home')


def event_create_view(request):
	if request.user.is_authenticated:
		event = CreateEventForm(request.POST or None)
		if event.is_valid():
			print("Model1")
			# print(event.user_id)
			# # venue_fetch = add_venue.objects.get(venue_name= event.venue)
			# event.venue = add_venue.objects.get(venue_name= event.venue)
			# # sport_fetch = add_sports.objects.get(sport_name= event.sport)
			# event.sport = add_sports.objects.get(sport_name= event.sport)
			# # event_cat_fetch = add_event_cat.objects.get(event_cat_name= event.event_category)
			# event.event_category = add_event_cat.objects.get(event_cat_name= event.event_category)
			event.save()
			event.user_id = request.user
			event.save()
			event = CreateEventForm()
		context = {
		'events': event
		}
		return render(request, "events/event-create.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the details of venues')
		return redirect('login')




