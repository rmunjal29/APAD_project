from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class user_profile(models.Model):
	# user_name = models.CharField(max_length=50) #max_length = required
	# email = models.CharField(max_length=60) 
	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	user1 = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')	
	contact_number = models.CharField(max_length=20)
	zip_code = models.CharField(max_length=8)
	# password1 = models.CharField(max_length=20)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		user_profile.objects.create(user1=instance)
	instance.profile.save()


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

	def get_absolute_url(self):
		return reverse("psevents:venue-detail", kwargs={"id": self.id})

class add_event_cat(models.Model):
	event_cat_name = models.CharField(max_length=100)

class add_sports(models.Model):
	sport_name = models.CharField(max_length=100)
	player_count = models.IntegerField()
	equip_req_flag = models.CharField(max_length=10)
	sport_desc = models.CharField(max_length=200)


class add_new_event(models.Model):
	event_category = models.ForeignKey(add_event_cat, null=True, on_delete=models.PROTECT)
	venue = models.ForeignKey(add_venue, null=True, on_delete=models.PROTECT)
	sport = models.ForeignKey(add_sports, null=True, on_delete=models.PROTECT)
	event_name = models.CharField(max_length=100)
	event_date = models.CharField(max_length=100)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	user_id = models.ForeignKey(User, default=1,  on_delete=models.PROTECT)
	host_flag = models.CharField(max_length=100, default=1,null=True)
	member_flag = models.CharField(max_length=100, default=0,null=True)
	event_desc = models.CharField(max_length=100, null=True)
	capacity_avail = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse("psevents:event-detail", kwargs={"id": self.id})

# class joined_event(models.Model):

# 	event_id = models.ForeignKey(add_new_event, null=True, on_delete=models.PROTECT)
# 	user_id = models.ForeignKey(User, on_delete=models.PROTECT)




