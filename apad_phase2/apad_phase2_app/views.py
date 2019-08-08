# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

import logging
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput

from apad_phase2_app.utils.forms import EmailForm
from apad_phase2_app.utils.forms import VenueForm
from apad_phase2_app.utils.apad_project_functions import admin_check, new_event, new_venue
from apad_phase2_app.utils.forms import CreateOrJoinForm
from apad_phase2_app.utils.forms import CreateEventForm
from apad_phase2_app.models import add_venue


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Ritika APAD app")


def emailForm(request):
    # if request.method == 'POST':
    #     form = EmailForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         return HttpResponse('/thanks/')
    # else:
    form = EmailForm()
    form_action = "venueFormPath"
    return render(request, 'venue_form.html', {'form': form, 'form_action': form_action})



def venueForm(request):
    # validate email here
    if not admin_check(request.POST.get('email_id', '')):
        error_message = 'Not an Admin. Enter email again'
        form_action = "venueFormPath"
        return render(request, 'venue_form.html',
                      {'form': EmailForm(), 'form_action': form_action, 'error_message': error_message})
    else:
        form_action = "insertVenuePath"
        return render(request, 'venue_form.html', {'form': VenueForm(), 'form_action': form_action})


def insertVenue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        venue = form.save()
        if form.is_valid():
            # venue = add_venue(venue_name='Zilkerr',address='az',zip_code='12356',contact_number='3456927894',description='gshj',open_time='12',close_time='22',games_total_count='4',games_available_count='4')
            # venue = form.save()
            # venue.refresh_from_db()
            form.save()
    # if new_venue(venue_details):
            return HttpResponse('New venue is created successfully')
    # new_venue(request.POST.get('venue_details', ''))

def createOrJoin(request):
    form = CreateOrJoinForm()
    form_action = "CreateEventPath"
    return render(request, 'create_join.html', {'form': form, 'form_action': form_action})

def createEvent(request):
    if request.POST.get('create_or_join', '') == 'create':
        form = CreateEventForm()
        form_action = "InsertEventPath"
        return render(request, 'create_join.html', {'form': form, 'form_action': form_action})

def insertNewEvent(request):
    # email_id = request.POST.get('email_id', '')
    # event_name = request.POST.get('event_name', '')
    # event_category = request.POST.get('event_category', '')
    # sports_category = request.POST.get('sports_category', '')
    # venue = request.POST.get('venue', '')
    # event_date = request.POST.get('event_date', '')
    # start_time = request.POST.get('start_time', '')
    # end_time = request.POST.get('end_time', '')
    # event_desc = request.POST.get('event_desc', '')
    # capacity = request.POST.get('capacity', '')
    #
    # new_event_details = [email_id, event_name,event_category,sports_category,venue,event_date,start_time,end_time,event_desc, capacity]
    # if new_event(new_event_details):
    #     return HttpResponse('New event is created successfully')

    if request.method == 'POST':
        form = CreateEventForm(request.POST)
        event = form.save()
        if form.is_valid():
            add_venue.venue_id = form.cleaned_data.get('venue_id')
            # venue = add_venue(venue_name='Zilkerr',address='az',zip_code='12356',contact_number='3456927894',description='gshj',open_time='12',close_time='22',games_total_count='4',games_available_count='4')
            # venue = form.save()
            # venue.refresh_from_db()
            form.save()
    # if new_venue(venue_details):
            return HttpResponse('New event is created successfully')
    # new_venue(request.POST.get('venue_details', ''))






