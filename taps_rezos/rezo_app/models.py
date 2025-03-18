from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    occasion = models.CharField(max_length=100)
    seat_id = models.CharField(max_length=50, blank=True, null=True)
    name= models.CharField(max_length=100)
    email= models.EmailField()

    def __str__(self):
        return f'Reservation for {self.guests} on {self.date} at {self.time}'


