from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import BookingSerializer, MenuItemSerializer
from .models import Booking, MenuItem
from rest_framework import permissions


def sayHello(request):
    return HttpResponse('Hello World')


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

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
