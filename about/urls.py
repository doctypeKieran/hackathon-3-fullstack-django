from django.urls import path
from about.views import about_page

urlpatterns = [
    path("", about_page, name='about_page'),
]