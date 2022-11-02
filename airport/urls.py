"""airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flights.views import FlightListView, UpcomingBookingListView, BookingDetailView, BookingUpdateView, BookingDeleteView, UserCreateAPIView, UserLoginAPIView, CreateFlightView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('flights/', FlightListView.as_view(), name='flight_list'),
    path('booking/', UpcomingBookingListView.as_view(), name='booking_list'),
    path('bookingdetails/<int:object_id>/',
         BookingDetailView.as_view(), name='booking_detail'),
    path('bookingdetails/<int:object_id>/update/',
         BookingUpdateView.as_view(), name='booking_update'),
    path('bookingdetails/<int:object_id>/delete',
         BookingDeleteView.as_view(), name='booking_delete'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='log_in'),
    path('bookflight/', CreateFlightView.as_view(), name='book-flight'),


]
