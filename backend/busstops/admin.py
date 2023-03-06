from django.contrib import admin
from .models import BusStops

class BusStopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(BusStops, BusStopsAdmin)
