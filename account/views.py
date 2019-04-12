from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from .models import Profile
from django.contrib import messages
from django.conf import settings


# Create your views here.
def user_login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			lf = form.cleaned_data
			user = authenticate(username=lf['username'],password=lf['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('invalid login')
		else:
			form = LoginForm()
	return render(request, 'account/login.html',{'form':form})


@login_required
def dashboard(request):
	prof = get_object_or_404(Profile, user=request.user.username)
	return render(request, 'account/dashboard.html',{'section':dashboard,'prof':prof})

def load_profile(user):
  try:
    return user.profile
  except:  # this is not great, but trying to keep it simple
    profile = Profile.objects.create(user=user)
    return profile


def register(request):
	form  = UserRegistrationForm()
	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			check = User.objects.filter(username=username).first()
			if (password == password2):
				if check:
					messages.success(request,'Error Passwords do not match!!!')
					return redirect('register')
				else:
					new_user = User(username=username,email=email, password=make_password(password,salt=None,hasher='default'))
					new_user.save()
					profile = Profile.objects.create(user=new_user)
					return render(request, 'account/register_done.html', {'new_user':new_user})
		else:
			form = UserRegistrationForm()
			messages.success(request,'Registration failed, please try again!!!')
			return render(request,'account/register.html',{'form': form})
	return render(request,'account/register.html',{'form': form})



@login_required
def edit(request):
	user_form = UserEditForm()
	profile_form = ProfileEditForm()

	if request.method == 'POST':
		user_form = ProfileEditForm(request.POST or None,instance=request.user )
		profile_form = UserEditForm(request.POST or None, instance=request.user.profile, files=request.FILES)
		inst_user = User.objects.all().filter(username=request.user).values
		inst_prof = Profile.objects.all().filter(user=request.user.profile.user).values

		if user_form.is_valid() and profile_form.is_valid():
			user_form = ProfileEditForm(request.POST ,instance=request.user)
			profile_form = UserEditForm(request.POST, instance=request.user.profile, files=request.FILES)
			user_form.save()
			profile_form.save()
			messages.success(request,'Profile updated successfully')
			return redirect(reverse('dashboard'))
		else:
			messages.error(request,'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})



def logout(request):
	logout(request)
	context = locals()
	return render(request,'registration/logged_on.html',context)

	
@login_required
def profile(request):
	u_form = UserEditForm()
	p_form = ProfileEditForm()
	if request.method == 'POST':
		u_form = UserEditForm(request.POST, instance=request.user)
		p_form = ProfileEditForm(request.POST,request.FILES,
			instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,'Profile updated successfully')
			return redirect(reverse('dashboard'))

	else:
		u_form = UserEditForm(instance=request.user)
		p_form = ProfileEditForm(instance=request.user.profile)
		

	context={'u_form':u_form,'p_form':p_form}
	return render(request, 'account/edit.html',context)