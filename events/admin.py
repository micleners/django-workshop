from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter', 'time', 'location')

admin.site.register(Event, EventAdmin)
