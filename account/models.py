from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	sex = models.CharField(max_length=20, blank=True)
	photo = models.ImageField(default="user.png",upload_to='users/%Y/%m/%d', blank=True, null=True)
	
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)


	#def save(self, **kwargs):
	    #super().save()
	def save(self, *args, **kwargs):
	    super().save(*args, **kwargs)
	   
	    img = Image.open(self.photo.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (300,300)
	        img.thumbnail(output_size)
	        img.save(self.photo.path)


