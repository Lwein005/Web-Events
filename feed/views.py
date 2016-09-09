from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import EventForm
from .models import Event

# Create your views here.

def event_create(request):
	form = EventForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not Successfully Created")
	context = {
		"form": form,
	}
	return render(request, "feed/event_form.html", context)

def event_description(request, id=None):
	instance = get_object_or_404(Event, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "feed/event_detail.html", context)

def event_list(request):
	queryset = Event.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}


	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User list"
	# 	}
	# 	return render(request, "feed/index.html", context)
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}
	return render(request, "feed/event_list.html", context)

def event_update(request, id=None):
	instance = get_object_or_404(Event, id=id)
	form = EventForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Successfully Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "feed/event_form.html", context)

def event_delete(request, id=None):
	instance = get_object_or_404(Event, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("feed:list")