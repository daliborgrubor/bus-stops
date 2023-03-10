from django.contrib import admin
from .models import BusStops

class BusStopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'longitude', 'latitude')

admin.site.register(BusStops, BusStopsAdmin)