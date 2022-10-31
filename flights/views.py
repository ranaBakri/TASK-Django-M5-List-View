from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import FlightsListSerializer, BookingListSerializer
from django.utils import timezone


class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer


class UpcomingBookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer


class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = BookingListSerializer


class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class BookingCreateView(CreateAPIView):
    serializer_class = BookingListSerializer
