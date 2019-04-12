from django.urls import path, include
from . import views 
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [

		#path('login/', views.user_login, name='login'),
		#path('dashboard/',views.dashboard, name='dashboard'),
		#path('login/', 'django.contrib.auth.views.login', name='login'),
		#path('login/', auth_view.login, {'template_name': 'login.html'}, name='login'),
		#path('logout/','django.contrib.auth.views.logout', name='logout'),
		#path('logout-then-login/','auth_view.logout_then_logout',name='logout_then_login'),
		#path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
		#path('login/', auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
		#path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
		path('',TemplateView.as_view(template_name='account/dashboard.html'),name='dashboard'),
		path('register/',views.register,name='register'),
		path('registration_done/',TemplateView.as_view(template_name='account/register_done.html')),
		path('edit/',views.profile, name='edit'),
		path('login/',LoginView.as_view(),name='login'),
		path('logout/',LogoutView.as_view(), name='logout'),
		path('password_change/',PasswordChangeView.as_view(),name='password_change'),
		path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
		path('password_reset/',PasswordResetView.as_view(), name='password_reset'),
		path('password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
		path('password_reset/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
		path('password_reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),


]
