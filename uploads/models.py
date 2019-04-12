from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class SportsModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	sports_title = models.CharField(max_length = 50)
	image_name = models.ImageField(upload_to = 'sports_picture_files/%Y/%m/%d', blank = True, null=True)

	def __str__(self):
		return self.sports_title
	
class ClubsModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	club_title = models.CharField(max_length = 50)
	image_name = models.ImageField(upload_to = 'clubs_picture_files/%Y/%m/%d',blank=True)

	def __str__(self):
		return self.club_title

class AcademicModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	academic_title = models.CharField(max_length = 50)
	image_name = models.ImageField(upload_to = 'academic_picture_files/%Y/%m/%d',blank=True)

	def __str__(self):
		return self.academic_title

class EventsModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	events_title = models.CharField(max_length = 50)
	image_name = models.ImageField(upload_to = 'events_picture_files/%Y/%m/%d',blank=True)

	def __str__(self):
		return self.events_title
