from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadImageForm
from .models import AcademicModel, SportsModel, ClubsModel, EventsModel
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def upload_image(request):
	form = UploadImageForm()
	if request.method == "POST":
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			selection = form.cleaned_data['selection']
			if(selection == 'Academic'):

				academic = AcademicModel(academic_title=form.cleaned_data['title'],image_name = request.FILES['image_name'])
				academic.save()
				messages.success(request, "Academic picture uploaded successfully")
				return redirect('dashboard')
			elif(selection == 'Clubs'):
				clubs = ClubsModel(club_title=form.cleaned_data['title'],image_name = request.FILES['image_name'])
				clubs.save()
				messages.success(request, "Clubs picture uploaded successfully")
				return redirect('dashboard')
			elif(selection == 'Sports'):
				sports = SportsModel(sports_title=form.cleaned_data['title'],image_name = request.FILES['image_name'])
				sports.save()
				messages.success(request, "Sports picture uploaded successfully")
				return redirect('dashboard')
			elif(selection == 'Events'):
				events = EventsModel(events_title=form.cleaned_data['title'],image_name = request.FILES['image_name'])
				events.save()
				messages.success(request, "Events picture uploaded successfully")
				return redirect('dashboard')
			else:
				messages.warning(request, "Unkown selected field")
			return redirect('dashbaord')
		else:
			messages.error(request, 'Failed to validate file')
			return redirect(reverse('upload_image'))
	else:
		return	render(request, 'uploads/upload_image.html', {'form':form})