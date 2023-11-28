from django import forms
import datetime 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, STAFF, GENERAL_USER
class BaseUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,error_messages={'required': 'Please provide an email address.'})
    phone_number = forms.CharField(max_length=15,required=True, error_messages={'required': 'Please provide a phone number.', 'max_length': 'Phone number must be 11 digits long.'})
    age = forms.IntegerField(required=True,min_value=18, error_messages={'required': 'Please provide your age.', 'min_value': 'You must be at least 18 years old.'})

    class Meta(UserCreationForm.Meta):
        model=User
        fields =UserCreationForm.Meta.fields + ('email','phone_number','age')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.age = self.cleaned_data['age']
            user_profile.phone_number = self.cleaned_data["phone_number"]
            user_profile.save()
        return user
class StaffUserCreationForm(BaseUserCreationForm):
    badge_number = forms.CharField(max_length=5, required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.role = STAFF
            user_profile.badge_number = self.cleaned_data["badge_number"]
            user_profile.save()
        return user
class GeneralUserCreationForm(BaseUserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.role = GENERAL_USER
            user_profile.save()
        return user