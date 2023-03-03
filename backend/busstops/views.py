from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StopPointSerializer
from .models import StopPoint

# Create your views here.

class StopPointView(viewsets.ModelViewSet):
    serializer_class = StopPointSerializer
    queryset = StopPoint.objects.all()
