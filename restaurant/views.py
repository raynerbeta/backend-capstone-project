from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer


def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    def get(self, request):
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
