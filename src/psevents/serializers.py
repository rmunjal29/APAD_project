from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id ','username', 'email','password')


class VenueSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_venue
		fields = ('id','venue_name','address', 'zip_code', 'contact_number','description','open_time','close_time','games_total_count','games_available_count')


class EventCatSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_event_cat
		fields = ('id','event_cat_name',)


class SportSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_sports
		fields = ('id','sport_name', 'player_count', 'equip_req_flag', 'sport_desc')


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = add_new_event
		fields = ('id','event_category', 'sport', 'venue', 'event_name', 'event_date', 'start_time', 'end_time', 'user_id', 'host_flag', 'member_flag','event_desc', 'capacity_avail')