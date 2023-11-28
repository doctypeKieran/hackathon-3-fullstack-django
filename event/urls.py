from django.urls import path
from event.views import create_event, view_events, join_event, manage_bookings, approve_booking,user_bookings

urlpatterns = [
    path('create-event/', create_event, name='create_event'),
    path('', view_events, name='events-list'),
    path('event-list/', view_events, name='event-list'),
    path('join-event/<int:event_id>/', join_event, name='join_event'),  # New path for joining an event
    path('manage-bookings/', manage_bookings, name='manage_bookings'),  # New path for managing bookings
    path('approve-booking/<int:booking_id>/', approve_booking, name='approve_booking'),  # New path for approving a booking
    path('user-bookings/', user_bookings, name='user_bookings'),
]