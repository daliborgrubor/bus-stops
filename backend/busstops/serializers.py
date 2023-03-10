from rest_framework import serializers
from .models import BusStops

class BusStopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStops
        fields = ('id', 'title', 'longitude', 'latitude')
