from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserForm, VenueForm
from .models import add_venue


@login_required
def home(request):
	return render(request, 'home.html')

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
	
	venue_form = VenueForm(request.POST or None)
	if venue_form.is_valid():
		venue_form.save()
		venue_form = VenueForm()
	context = {
	'form': venue_form
	}
	return render(request, "venues/venue-create.html", context)



def venue_update_view(request, id=id):
	obj = get_object_or_404(add_venue, id=id)
	update_form = VenueForm(request.POST or None, instance=obj)
	if update_form.is_valid():
		update_form.save()
	context = {
		'form': update_form
	}
	return render(request, "venues/venue-create.html", context)


def venue_list_view(request):
	queryset = add_venue.objects.all() # list of objects
	context = {
		"object_list": queryset
	}
	return render(request, "venues/venue-list.html", context)


def venue_detail_view(request, id):
	obj = get_object_or_404(add_venue, id=id)
	context = {
		"object": obj
	}
	return render(request, "venues/venue-detail.html", context)


def venue_delete_view(request, id):
	obj = get_object_or_404(add_venue, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "venues/venue-delete.html", context)


	




