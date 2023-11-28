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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user1_profile')
    role = models.CharField(max_length=5, choices=USER_ROLES, default=GENERAL_USER)
    badge_number = models.CharField(max_length=5, blank=True, null=True) 
    # CREATE EMAIL FIELD
    phone_number = models.CharField(max_length=15) 
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=255)
    def save(self, *args, **kwargs):
        if self.role == STAFF and not self.badge_number:
            raise ValidationError(_('Staff members must have a badge number.'))
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.user1_profile.save()