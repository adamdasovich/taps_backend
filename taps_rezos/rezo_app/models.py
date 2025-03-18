from django.db import models
import datetime
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
        return f'Reservation for {self.guests} on {self.date} at {self.time} because I said'
    
class MoviePoll(models.Model):
    week_start = models.DateField(unique=True, default=datetime.date.today())  # Start of the week (Monday)
    movie1 = models.CharField(max_length=255)
    movie2 = models.CharField(max_length=255)
    movie3 = models.CharField(max_length=255)
    movie1_votes = models.IntegerField(default=0)
    movie2_votes = models.IntegerField(default=0)
    movie3_votes = models.IntegerField(default=0)
    winning_movie = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Poll for week starting {self.week_start}"

    def calculate_winner(self):
        votes = {
            self.movie1: self.movie1_votes,
            self.movie2: self.movie2_votes,
            self.movie3: self.movie3_votes,
        }
        if votes[self.movie1] == 0 and votes[self.movie2] == 0 and votes[self.movie3] == 0:
          self.winning_movie = None
          self.save()
          return
        self.winning_movie = max(votes, key=votes.get)
        self.save()

    @staticmethod
    def get_current_poll():
        today = timezone.now().date()
        monday = today - datetime.timedelta(days=today.weekday())
        try:
            return MoviePoll.objects.get(week_start=monday)
        except MoviePoll.DoesNotExist:
            return None

    @staticmethod
    def create_new_poll(movie1, movie2, movie3):
        today = timezone.now().date()
        monday = today - datetime.timedelta(days=today.weekday())
        MoviePoll.objects.create(week_start=monday, movie1=movie1, movie2=movie2, movie3=movie3)





