"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from account.views import register
from django.conf.urls.static import static
from navigation.views import about, index, service, contact, academic, clubs, events, sports
from uploads.views import upload_image
from django.contrib.auth.views import LoginView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', )),
    path('account/', include('account.urls')),
    path('upload/',include('uploads.urls')),
    path('image/', include('image.urls')),
    path('',index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/',about, name='about'),
    path('service/', service, name='service'),
    path('register/', register, name='register'),
    path('academic/', academic, name='academic'),
    path('clubs/',clubs, name='clubs'),
    path('events/', events, name='events'),
    path('sports/', sports, name='sports'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)