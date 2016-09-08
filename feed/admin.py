from django.contrib import admin

# Register your models here.
from feed.models import Event
admin.site.register(Event)
