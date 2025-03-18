from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
import datetime

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    @action(detail=False, methods=['get'])
    def reserved_seats(self, request):
        """
        Get all reserved seats for a specific date and time.
        Query parameters:
        - date: YYYY-MM-DD
        - time: HH:MM or HH:MM:SS
        """
        date_str = request.query_params.get('date')
        time_str = request.query_params.get('time')
        
        if not date_str or not time_str:
            return Response(
                {"error": "Both date and time parameters are required"},
                status=400
            )
        
        try:
            # Handle time format - frontend might send HH:MM without seconds
            if len(time_str.split(':')) == 2:
                time_str = f"{time_str}:00"
                
            # Find all reservations for this date and time
            reservations = Reservation.objects.filter(
                date=date_str,
                time=time_str
            )
            
            # Debug information
            print(f"Date: {date_str}, Time: {time_str}")
            print(f"Found {reservations.count()} reservations")
            
            # Collect all reserved seat IDs
            reserved_seats = []
            for reservation in reservations:
                if reservation.seat_id:
                    # Split the seat_id field directly instead of using the property
                    if ',' in reservation.seat_id:
                        seats = [seat.strip() for seat in reservation.seat_id.split(',')]
                        reserved_seats.extend(seats)
                    else:
                        # Handle single seat case
                        reserved_seats.append(reservation.seat_id.strip())
            
            return Response({
                "date": date_str,
                "time": time_str,
                "reserved_seats": reserved_seats
            })
            
        except Exception as e:
            print(f"Error in reserved_seats: {str(e)}")
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=400
            )
class MoviePollView(generics.RetrieveAPIView):
    serializer_class = MoviePollSerializer

    def get_object(self):
        return MoviePoll.get_current_poll()

class VoteView(generics.UpdateAPIView):
    queryset = MoviePoll.objects.all()
    serializer_class = MoviePollSerializer

    def update(self, request, *args, **kwargs):
        poll = self.get_object()
        movie = request.data.get('movie')

        if movie == poll.movie1:
            poll.movie1_votes += 1
        elif movie == poll.movie2:
            poll.movie2_votes += 1
        elif movie == poll.movie3:
            poll.movie3_votes += 1
        else:
            return Response({'error': 'Invalid movie choice'}, status=status.HTTP_400_BAD_REQUEST)

        poll.calculate_winner()
        poll.save()
        serializer = self.get_serializer(poll)
        return Response(serializer.data)

class CreateNewPollView(generics.CreateAPIView):
    serializer_class = MoviePollSerializer

    def create(self, request, *args, **kwargs):
        today = datetime.date.today()
        weekday = today.weekday()
        # if weekday != 2: # 2 is Wednesday
        #     return Response({'error': 'Poll creation is only allowed on Wednesdays.'}, status=status.HTTP_400_BAD_REQUEST)

        movie1 = request.data.get('movie1')
        movie2 = request.data.get('movie2')
        movie3 = request.data.get('movie3')

        if not all([movie1, movie2, movie3]):
            return Response({'error': 'Movie titles are required.'}, status=status.HTTP_400_BAD_REQUEST)

        MoviePoll.create_new_poll(movie1, movie2, movie3)
        return Response({'message': 'New poll created successfully.'}, status=status.HTTP_201_CREATED)
        
