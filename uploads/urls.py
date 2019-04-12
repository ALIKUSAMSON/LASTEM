from . import views
from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'uploads'

urlpatterns=[
	path('',views.upload_image, name='upload_image'),
	#path('',TemplateView.as_view(template_name='navigation/upload_image.html'),name='upload_image'),

]

