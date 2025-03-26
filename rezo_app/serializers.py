from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class MoviePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoll
        fields = '__all__'