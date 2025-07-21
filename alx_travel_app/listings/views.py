from rest_framework import generics
from .models import Listing, Booking, Review, User
from .serializers import (
    ListingSerializer, BookingSerializer, ReviewSerializer, UserSerializer
)

class ListingList(generics.ListCreateAPIView):
    """
    View to list all listings or create a new listing.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific listing.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingList(generics.ListCreateAPIView):
    """
    View to list all bookings or create a new booking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific booking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewList(generics.ListCreateAPIView):
    """
    View to list all reviews or create a new review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserList(generics.ListCreateAPIView):
    """
    View to list all users or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a specific user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
