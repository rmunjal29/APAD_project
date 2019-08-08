from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import add_venue

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