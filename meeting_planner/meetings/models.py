from datetime import time

from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    start_time = models.TimeField(default=time(hour=9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} @ {self.start_time} on {self.date} for {self.duration} hour(s)"