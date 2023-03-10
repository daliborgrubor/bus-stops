from django.db import models

class BusStops(models.Model):
    title = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def _str_(self):
        return self.title
