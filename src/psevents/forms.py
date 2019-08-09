from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import DateInput

class UserForm(UserCreationForm):
	# user_name = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
	email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.')
	contact_number = forms.CharField(max_length=20)
	zip_code = forms.CharField(max_length=8)
	# password1 = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'contact_number', 'zip_code', 'password1', 'password2')

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = user
# 		fields = ('user_name', 'password1')


class VenueForm(forms.ModelForm):
	venue_name = forms.CharField(label='Please Enter the venue name')
	address = forms.CharField(label='Please Enter the venue address', max_length=100)
	zip_code = forms.CharField(label='Venue zip code', max_length=100)
	contact_number = forms.CharField(label='Please provide a contact number', max_length=100)
	description = forms.CharField(label='Enter the venue description (not more than 200 characters)', max_length=100)
	open_time = forms.CharField(label='Please Enter the open time in 24hrs format (Only the hour)', max_length=100)
	close_time = forms.CharField(label='Please Enter the close time in 24hrs format: (Only the hour)', max_length=100)
	games_total_count = forms.CharField(label='Please enter the total number of games that can be played in single time slot', max_length=100)
	games_available_count = forms.CharField(label='Please enter the available number of games that can be played in single time slot', max_length=100)

	class Meta:
		model = add_venue
		fields = ('venue_name','address', 'zip_code', 'contact_number','description','open_time','close_time','games_total_count','games_available_count')


class event_cat(forms.ModelForm):
	event_cat_name = forms.CharField(label = "Please enter the event category: ", max_length=100)

	class Meta:
		model = add_event_cat
		fields = ('event_cat_name',)



class sports(forms.ModelForm):
	sport_name = forms.CharField(label = "Please enter the sport name: ", max_length=100)
	player_count = forms.IntegerField(label = "Please enter the max player count: ")
	equi_req_flag = forms.CharField(label="Please enter if equipments are required 0: No, 1: Yes")
	sport_desc = forms.CharField(label="Please enter the sport description", max_length=200)
	class Meta:
		model = add_sports
		fields = ('sport_name', 'player_count', 'equi_req_flag', 'sport_desc')


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateEventForm(forms.ModelForm):
	# event_cat_dd = fetch_event_cat()
	# sports_cat_dd = fetch_sport()
	# venue_dd = fetch_venue()

	# email_id = forms.CharField(label='Please Enter the email id', max_length=100)
	event_name = forms.CharField(label='Please Enter the Event Name', max_length=100)

	event_category = forms.ModelChoiceField(queryset=add_event_cat.objects.all(), empty_label="(Nothing)")
	

	# event_category = forms.CharField(label='Event Category', widget=forms.Select(choices=event_cat_dd))
	# sports_category = forms.CharField(label='Sports Category', widget=forms.Select(choices=sports_cat_dd))

	sport = forms.ModelChoiceField(queryset=add_sports.objects.all(), empty_label="(Nothing)")

	# venue = forms.CharField(label='Select the Venue', widget=forms.Select(choices=venue_dd))

	venue = forms.ModelChoiceField(queryset=add_venue.objects.all(), empty_label="(Nothing)")

	
	# def __init__(self,user, *args, **kwargs):

	# 	super(CreateEventForm, self).__init__(*args, **kwargs)
	# 	self.fields['venue'].queryset = add_venue.objects.all()
	# 	self.fields['event_category'].queryset = add_event_cat.objects.all()
	# 	self.fields['sport'].queryset = add_sports.objects.all()

	def __init__(self, *args, **kwargs):
		super(CreateEventForm, self).__init__(*args, **kwargs)
		queryset = self.fields['venue'].queryset
		choices = [(poll.pk, poll.venue_name) for poll in queryset]
		self.fields['venue'].choices = choices

		queryset = self.fields['sport'].queryset
		choices = [(poll.pk, poll.sport_name) for poll in queryset]
		self.fields['sport'].choices = choices

		queryset = self.fields['event_category'].queryset
		choices = [(poll.pk, poll.event_cat_name) for poll in queryset]
		self.fields['event_category'].choices = choices


	event_date = forms.CharField(label='Please Enter the date in yyyy-mm-dd format', max_length=15)

	# event_date = forms.DateField(widget=DateInput(format='%Y-%m-%d'), input_formats=('%Y-%m-%d',), required=False)

	start_time = forms.CharField(label='Please Enter the start time in 24hrs format (Only the hour)', max_length=2)

	end_time = forms.CharField(label='Please Enter the end time in 24hrs format (Only the hour)', max_length=2)

	event_desc = forms.CharField(label='Please Enter the Event Description in not more than 200 words', max_length=200)

	capacity_avail = forms.CharField(label='Please Enter how many people can join', max_length=4)

	class Meta:
		model = add_new_event
		fields = ('event_name', 'event_category', 'sport', 'venue', 'event_date', 'start_time', 'end_time', 'event_desc', 'capacity_avail')



class FindSlotForm(forms.Form):
	venue = forms.ModelChoiceField(queryset=add_venue.objects.all(), empty_label="(Nothing)")

	def __init__(self, *args, **kwargs):
		super(FindSlotForm, self).__init__(*args, **kwargs)
		queryset = self.fields['venue'].queryset
		choices = [(poll.pk, poll.venue_name) for poll in queryset]
		self.fields['venue'].choices = choices

	event_date = forms.CharField(label='Please Enter the date in yyyy-mm-dd format', max_length=15)
	
	class Meta:	
		fields = ('venue', 'event_date')

class FindVenueForm(forms.Form):

	event_date = forms.CharField(label='Please Enter the date in yyyy-mm-dd format', max_length=15)
	start_time = forms.CharField(label='Please Enter the start time in 24hrs format (Only the hour)', max_length=2)
	end_time = forms.CharField(label='Please Enter the end time in 24hrs format (Only the hour)', max_length=2)
	
	class Meta:	
		fields = ('event_date', 'start_time', 'end_time')


class DeleteEventForm(forms.Form):

	event = forms.ModelChoiceField(queryset=add_new_event.objects.all(), empty_label="(Nothing)")
	def __init__(self, *args, **kwargs):
		super(DeleteEventForm, self).__init__(*args, **kwargs)
		queryset = self.fields['event'].queryset
		choices = [(poll.pk, poll.event_name) for poll in queryset]
		self.fields['event'].choices = choices

	class Meta:	
		fields = ('event',)


class FindEventForm(forms.Form):

	event_date = forms.CharField(label='Please Enter the date in yyyy-mm-dd format', max_length=15)
	start_time = forms.CharField(label='Please Enter the start time in 24hrs format (Only the hour)', max_length=2)
	end_time = forms.CharField(label='Please Enter the end time in 24hrs format (Only the hour)', max_length=2)
	zip_code = forms.CharField(label='Venue zip code', max_length=100)

	class Meta:	
		fields = ('event_date','start_time', 'end_time', 'zip_code')


class EventCatForm(forms.ModelForm):
	event_cat_name = forms.ModelChoiceField(queryset=add_event_cat.objects.all(), required=False)

	def __init__(self, *args, **kwargs):
		super(EventCatForm, self).__init__(*args, **kwargs)
		queryset = self.fields['event_cat_name'].queryset
		choices = [(poll.pk, poll.event_cat_name) for poll in queryset]
		self.fields['event_cat_name'].choices = choices

	class Meta:
		model = add_event_cat
		fields = ('event_cat_name',)
