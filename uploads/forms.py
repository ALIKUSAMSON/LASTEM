from django import forms

IMAGE_LOCATION = (
		('Clubs', 'Clubs'),
		('Sports', 'Sports'),
		('Events', 'Events'),
		('Academic', 'Aacademic'),
				)


class UploadImageForm(forms.Form):
	selection = forms.CharField(label = 'Select Gallery category', max_length=255, widget=forms.Select(choices=IMAGE_LOCATION))
	title = forms.CharField(label = 'Image title' ,max_length=50)
	image_name = forms.ImageField()


