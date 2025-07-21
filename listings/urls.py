from django.urls import path
from .views import *

urlpatterns = [
    path('listings/', ListingList.as_view(), name='listing-list'),
    path('listings/<int:pk>/', ListingDetail.as_view(), name='listing-detail'),
    path('bookings/', BookingList.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='booking-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]