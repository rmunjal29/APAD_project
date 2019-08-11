from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import *
from .models import *
from .project1 import *
import datetime
from datetime import timedelta
from django.template.defaulttags import register
from django.http import HttpRequest


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
			auth_login(request,user)
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
		messages.info(request, 'You are not authorized to add an event category! (Admin only activity)')
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
		messages.info(request, 'You are not authorized to add a sport! (Admin only activity)')
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
		messages.info(request, 'You are not logged in. Please login first to create an event')
		return redirect('login')


def slot_view(request):
	if request.user.is_authenticated:
		part1={}
		part2={}
		form = FindSlotForm(request.POST or None)
		if form.is_valid():
			venue = form.cleaned_data.get('venue')
			date = form.cleaned_data.get('event_date')	
			# print(venue.venue_name, date)
			venue_time = add_venue.objects.filter(venue_name=venue.venue_name).values('open_time','close_time')
			games_count = add_venue.objects.filter(venue_name=venue.venue_name).values('games_total_count')
			event_time = add_new_event.objects.filter(venue__venue_name__contains=venue.venue_name, event_date=date).values('start_time','end_time')

			# print(venue_time)
			# print(event_time)
			# print(event_times)
			# print(games_count[0]["games_total_count"])

			part1, part2 = find_booked_slots(venue.venue_name, date, venue_time, games_count, event_time)

			# find_booked_slots(venue, date, venue_time, games_count, event_time)
			# find_booked_slots()	
			flag=0

		else:
			flag=1

		context={'slots': form,
		'unfill_slots': part1,
		'fill_slots': part2,
		'flag' : flag
		}
		return render(request, "events/find-slot.html", context)

	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the available slots')
		return redirect('login')	

def venue_avail_view(request):
	if request.user.is_authenticated:
		avail_venues=[]
		form = FindVenueForm(request.POST or None)
		if form.is_valid():
			date = form.cleaned_data.get('event_date')	
			start_time = form.cleaned_data.get('start_time')	
			end_time = form.cleaned_data.get('end_time')
			venues = add_venue.objects.values_list('venue_name', flat=True)

			event_date_strp = datetime.datetime.strptime(date, '%Y-%m-%d').date()

			# print(venues)
			# print(start_time,end_time)

			for j in venues:
				venue_time = add_venue.objects.filter(venue_name=j).values('open_time','close_time')
				games_count = add_venue.objects.filter(venue_name=j).values('games_total_count')
				event_time = add_new_event.objects.filter(venue__venue_name__contains=j, event_date=date).values('start_time','end_time')

				temp1 = find_booked_slots(j, date, venue_time, games_count, event_time, debug=False)
				# print(temp1)
				if temp1==None:
					avail_venues.append(j)
				else:
					initial_time = datetime.datetime.strptime(start_time, '%H').time()
					finish_time = datetime.datetime.strptime(end_time, '%H').time()

					initial_datetime = datetime.datetime.combine(event_date_strp,initial_time)
					finish_datetime = datetime.datetime.combine(event_date_strp,finish_time)

					timestamp = (initial_datetime, finish_datetime)

					for items in temp1:
						if items == timestamp and temp1[items]!=0:
							avail_venues.append(j)

			flag=0

		else:
			flag=1

		context = {
		'form': form,
		'venues': avail_venues,
		'flag': flag
		}

		return render(request, "events/find-venues.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the available venues')
		return redirect('login')		



def event_view(request):
	if request.user.is_authenticated:
		events=None
		form = FindEventForm(request.POST or None)
		if form.is_valid():
			date = form.cleaned_data.get('event_date')	
			start_time = form.cleaned_data.get('start_time')	
			end_time = form.cleaned_data.get('end_time')
			zip_code = form.cleaned_data.get('zip_code')

			request.session['date'] = date
			request.session['start_time'] = start_time
			request.session['end_time'] = end_time
			request.session['zip_code'] = zip_code

		context = {
			"form": form,			
		}
		return render(request, "events/find-events.html", context)


	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the available events')
		return redirect('login')		





def event_delete_view(request):
	if request.user.is_superuser:
		form = DeleteEventForm(request.POST or None)
		if form.is_valid():
			event = form.cleaned_data.get('event')
			event.delete()
			return redirect('../../')
		context = {
			"form": form,
		}
		return render(request, "events/event-delete.html", context)
	else:
		messages.info(request, 'You are not authorized to delete a venue! (Admin only activity)')
		return redirect('home')

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]


def join_event_view(request):
	date = request.session['date']
	start_time = request.session['start_time'] 
	end_time = request.session['end_time'] 
	zip_code = request.session['zip_code'] 


	events = add_new_event.objects.filter(venue__zip_code__contains=zip_code, event_date = date, 
				start_time__gte=start_time, start_time__lte=end_time).values('id','event_name', 'event_desc', 'capacity_avail')


	form = EventCatForm(request.POST or None)
	if form.is_valid():
		event_id = request.POST.get("counter")
		# print(event_id)
		if event_id != None:
			member_flag = add_new_event.objects.filter(id=int(event_id)).values('member_flag').first()
			member_flag = int(member_flag["member_flag"])

			if member_flag==1:
				messages.info(request, 'You are already registered for the event!')
				return redirect('home')

			else:	
				add_new_event.objects.filter(id=int(event_id)).update(member_flag=1)
				capacity_avail = add_new_event.objects.filter(id=int(event_id)).values('capacity_avail').first()
				capacity_avail = int(capacity_avail["capacity_avail"])-1
				add_new_event.objects.filter(id=int(event_id)).update(capacity_avail=capacity_avail)

				messages.info(request, 'Congratulations, You are registered for the event!')
				return redirect('home')
				# events1.save("member_flag")
	

		

	context = {
	"events": events,
	"form": form

	}
	return render(request, "events/display-events.html", context)


def joined_event_view(request):
	if request.user.is_authenticated:
		events = add_new_event.objects.filter(member_flag=1).values('event_name', 'event_desc', 'start_time', 'end_time')

		context = {
			"events": events			
		}
		return render(request, "events/joined-events.html", context)


	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to view the joined events')
		return redirect('login')		
	

