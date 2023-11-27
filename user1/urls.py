from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
urlpatterns = [
     path('login/', LoginView.as_view(template_name='user1/login.html'),name='login'),
     path('register/<user_type>/', views.register, name='register'),
]