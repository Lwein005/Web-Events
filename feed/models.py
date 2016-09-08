from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Event(models.Model):
	host = models.ForeignKeu('auth.User')
	title = models.CharField(max_length=100)
	description = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	event_date = models.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
	image = models.FileField(null=True, blank=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title