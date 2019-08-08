from django import forms
from apad_phase2_app.models import add_venue, add_new_event


import sqlite3

import logging

from apad_phase2_app.utils.apad_project_functions import fetch_event_cat, fetch_sport, fetch_venue

logger = logging.getLogger(__name__)

class EmailForm(forms.Form):
    email_id = forms.CharField(label='Please enter your Email id', max_length=100)

class VenueForm(forms.ModelForm):
    venue_name = forms.CharField(label='Please Enter the venue name', max_length=100)
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
        fields = ('venue_name', 'address', 'zip_code', 'contact_number', 'description', 'open_time', 'close_time', 'games_total_count', 'games_available_count')

class CreateOrJoinForm(forms.Form):
    create_or_join_dd = [
        ('create', 'CREATE'),
        ('join', 'JOIN'),
    ]
    create_or_join = forms.CharField(label='Create/Join an event', widget=forms.Select(choices=create_or_join_dd))

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateEventForm(forms.ModelForm):
    event_cat_dd = fetch_event_cat()
    sports_cat_dd = fetch_sport()
    venue_dd = fetch_venue()

    email_id = forms.CharField(label='Please Enter the email id', max_length=100)
    event_name = forms.CharField(label='Please Enter the Event Name', max_length=100)
    event_category = forms.CharField(label='Event Category', widget=forms.Select(choices=event_cat_dd))
    sports_category = forms.CharField(label='Sports Category', widget=forms.Select(choices=sports_cat_dd))
    venue = forms.CharField(label='Select the Venue', widget=forms.Select(choices=venue_dd))
    event_date = forms.DateField(widget=DateInput(format='%Y-%m-%d'), input_formats=('%Y-%m-%d',), required=False)
    start_time = forms.CharField(label='Please Enter the start time in 24hrs format (Only the hour)', max_length=2)
    end_time = forms.CharField(label='Please Enter the end time in 24hrs format (Only the hour)', max_length=2)
    event_desc = forms.CharField(label='Please Enter the Event Description in not more than 200 words', max_length=200)
    capacity = forms.CharField(label='Please Enter how many people can join', max_length=4)

    class Meta:
        fields = ["event_date", ]
        widgets = {
            'event_date': DateInput(),
        }
        model = add_new_event
        fields = ('email_id', 'event_name', 'event_category', 'sports_category', 'venue', 'event_date', 'start_time', 'end_time', 'event_desc', 'capacity')


