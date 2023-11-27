from django.urls import path 
from .views import create_event,join_event, view_events 
from . import views
urlpatterns= [
    path('create-event/', create_event, name='create_event'),
    path('join_event/<int:event_id>/', views.join_event, name='join_event'),
    path('', view_events, name='events-list'),
    path('event-list/', view_events, name='event-list'),
]