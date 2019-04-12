from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from uploads.models import AcademicModel, SportsModel, ClubsModel, EventsModel

# Create your views here.

def index(request):
	template = 'navigation/index.html'
	context = locals()
	return render(request, template, context)


def contact(request):
	template = 'navigation/contact.html'
	context = locals()
	return render(request, template, context)

def about(request):
	template = 'navigation/about.html'
	return render(request, template, context)


def service(request):
	template = 'navigation/service.html'
	context = locals()
	return render(request, template, context)

def sports(request):
	sports = SportsModel.objects.all()
	context = {'sports':sports}
	template = 'navigation/sports.html'
	return render(request, template, context)

def clubs(request):
	clubs = ClubsModel.objects.all()
	context = {'clubs':clubs}
	template = 'navigation/clubs.html'
	return render(request, template, context)


def events(request):
	events = EventsModel.objects.all()
	context = {'events':events}
	template = 'navigation/events.html'
	return render(request, template, context)

def academic(request):
	academic = AcademicModel.objects.all()
	context = {'academic':academic}
	template = 'navigation/academic.html'
	return render(request, template, context)

@login_required
def post_share(request, post_id):
	form = EmailPostForm()
	post = get_object_or_404(Post, id=post_id, status='publish')
	sent=False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],cd['email'],post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title,post_url,cd['name'],cd['comments'])
			send_mail(subject, message, 'dengima2013@gmail.com',[cd['to']])
			sent = True
			return render(request, 'blog/post/share.html',{'post':post,'form':form,'sent':sent})
		else:
			return Http404()
	return render(request, 'blog/post/share.html',{'post':post,'form':form,'sent':sent})