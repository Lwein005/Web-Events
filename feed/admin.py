from django.contrib import admin

# Register your models here.
from feed.models import Event

class EventModelAdmin(admin.ModelAdmin):
	list_display = ["host", "title", "timestamp", "event_date"]
	list_filter = ["event_date"]
	search_fields = ["title", "description"]
	class Meta:
		model = Event


admin.site.register(Event, EventModelAdmin)
