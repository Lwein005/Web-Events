from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your models here.

class Event(models.Model):
	host = models.ForeignKey('auth.User', null=True)
	title = models.CharField(max_length=100)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	event_date = models.DateTimeField(default=datetime.now, blank=True)
	image = models.FileField(null=True, blank=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("feed:event_description", kwargs={"id": self.id})
		