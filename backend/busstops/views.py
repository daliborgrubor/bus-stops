from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BusStopsSerializer
from .models import BusStops

class BusStopsView(viewsets.ModelViewSet):
    serializer_class = BusStopsSerializer
    queryset = BusStops.objects.all()
