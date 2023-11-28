from django.http import HttpRequest
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import MenuSerializer
from .models import Booking, Menu


def index(request: HttpRequest):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def reservations(request: HttpRequest):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)

    return render(request, "reservations.html", {"bookings": booking_json})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Booking.objects.all()
