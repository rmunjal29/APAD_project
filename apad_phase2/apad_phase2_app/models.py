from django.db import models
#
# class EventDate(models.Model):
#     event_date = models.DateTimeField(help_text='Event Date', null=True)
class add_venue(models.Model):
	# venue_id = forms.CharField(max_length=20)
	venue_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=100)
	description = models.CharField(max_length=100, null=True)
	open_time = models.CharField(max_length=100)
	close_time = models.CharField(max_length=100)
	games_total_count = models.CharField(max_length=100)
	games_available_count = models.CharField(max_length=100)

class add_new_event(models.Model):
	event_cat_id = models.CharField(max_length=100)
	venue_id = models.CharField(max_length=100)
	event_name = models.CharField(max_length=100)
	date = models.CharField(max_length=100)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	user_id = models.CharField(max_length=100)
	host_flag = models.CharField(max_length=100)
	member_flag = models.CharField(max_length=100)
	sports_Cat_id = models.CharField(max_length=100)
	event_desc = models.CharField(max_length=100, null=True)
	capacity_avail = models.CharField(max_length=100)