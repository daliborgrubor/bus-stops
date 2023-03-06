from django.contrib import admin
from .models import BusStops

class BusStopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'latitude', 'longitude')

admin.site.register(BusStops, BusStopsAdmin)
