from django.db import models

class BusStops(models.Model):
    title = models.CharField(max_length=120)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.title
