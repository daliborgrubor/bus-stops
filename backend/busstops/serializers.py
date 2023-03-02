from rest_framework import serializers
from .models import StopPoint

class StopPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopPoint
        fields = ('id', 'title', 'description', 'completed')
