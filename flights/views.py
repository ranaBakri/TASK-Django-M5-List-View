from ast import Delete
from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import FlightsListSerializer, BookingListSerializer, BookingUpdateSerializer
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


class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
