from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('poll/', MoviePollView.as_view(), name='movie-poll'),
    path('poll/<int:pk>/vote/', VoteView.as_view(), name='vote'),
    path('poll/create/', CreateNewPollView.as_view(), name='create-poll'),

]