from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
# Fix import if broken
ADMIN = 'ADMIN'
STAFF = 'STAFF'

GENERAL_USER = 'USER'
USER_ROLES = [
    (STAFF, _('Staff')),
    (GENERAL_USER, _('General User')),
    (ADMIN,'Admin'),
]

# Create your models here.
# Adding Models in from ideation 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='event_profile')
    role = models.CharField(max_length=5, choices=USER_ROLES, default=GENERAL_USER)
    badge_number = models.CharField(max_length=5, blank=True, null=True) 
    # CREATE EMAIL FIELD
    phone_number = models.CharField(max_length=15, blank=True, null=True,default='Not Provided') 
    age = models.PositiveIntegerField(blank=True, null=True,default='5')
    def save(self, *args, **kwargs):
        if self.role == STAFF and not self.badge_number:
            raise ValidationError(_('Staff members must have a badge number.'))
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"



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
        if approving_user.userprofile.role == STAFF:
            if not self.approved:
                self.approved = True
                self.session.capacity = F('capacity') - 1
                self.session.save()
                self.save()
        else:
            raise ValidationError(_('Only staff members can approve bookings.'))

