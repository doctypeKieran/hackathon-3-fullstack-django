from django.urls import path
from .views import gallery as gallery_view


urlpatterns = [
    path('', gallery_view, name='gallery'),
]