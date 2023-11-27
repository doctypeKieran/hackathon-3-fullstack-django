from django.urls import path 
from .views import create_event,join_event

urlspatterns= [
    path('create-event/',create_event, name='create_event'),
    path('join-event/', join_event, name='join_event'),
]