from __future__ import unicode_literals

from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length = 10)
    day_1_day = models.CharField(max_length = 100)
    day_1_day_price = models.PositiveIntegerField()
    day_1_night = models.CharField(max_length = 100)
    day_1_night_price = models.PositiveIntegerField()
    day_2_day = models.CharField(max_length = 100)
    day_2_day_price = models.PositiveIntegerField()
    day_2_night = models.CharField(max_length = 100)
    day_2_night_price = models.PositiveIntegerField()
    day_3_day = models.CharField(max_length = 100)
    day_3_day_price = models.PositiveIntegerField()
    day_3_night = models.CharField(max_length = 100)
    day_3_night_price = models.PositiveIntegerField()
    
    def __str__(self):
    	return self.name
