
from django.db import models
from user1.models import UserProfile 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

ADMIN = 'ADMIN'
STAFF = 'STAFF'

GENERAL_USER = 'USER'
# Create your models here.
# Adding Models in from ideation 

class RageRoomSession(models.Model):
    facilitator = models.ForeignKey('user1.UserProfile', on_delete=models.SET_NULL, null=True, related_name='facilitated_sessions')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    capacity = models.IntegerField(default=10)  
    image = models.ImageField(upload_to='rage_room_images/', blank=True, null=True)
    def __str__(self):
        return f"{self.title} on {self.date}"

    def save(self, *args, **kwargs):
        if self.capacity < 0:
            raise ValidationError("Capacity cannot be negative")
        super().save(*args, **kwargs)
class Booking(models.Model):
    session = models.ForeignKey(RageRoomSession, on_delete=models.CASCADE, related_name='bookings')
    participant = models.ForeignKey('user1.UserProfile', on_delete=models.CASCADE, related_name='bookings')
    booking_time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
     super(Booking, self).save(*args, **kwargs)


    def approve_booking(self, approving_user):
        if approving_user.user1_profile.role == STAFF:
            if not self.approved and self.session.capacity > 0:
                self.approved = True
                self.session.capacity -= 1
                self.session.save()
                self.save()
            elif self.session.capacity <= 0:
                raise ValidationError('No more capacity available for this session.')

        else:
            raise ValidationError(_('Only staff members can approve bookings.'))
    
    

