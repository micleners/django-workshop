from django.contrib import admin
from .models import Event, Location

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter', 'time', 'location')
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
