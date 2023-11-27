from django import forms
import datetime 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, STAFF, GENERAL_USER

class StaffUserCreationForm(UserCreationForm):
    badge_number=forms.CharField(max_length=10,required=False)
    age = forms.IntegerField(required=False)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email','age')
        email = forms.EmailField(required=False)
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.user1_profile.age = self.cleaned_data['age']
            user.user1_profile.role = STAFF
            if self.cleaned_data.get("badge_number"):
                user.user1_profile.badge_number = self.cleaned_data["badge_number"]
            user.user1_profile.save()
            
        return user
class GeneralUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    
    class Meta(UserCreationForm.Meta):
        model=User
        fields=UserCreationForm.Meta.fields + ('email','phone_number')
        email = forms.EmailField(required=False)
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.user1_profile.phone_number = self.cleaned_data['phone_number']
            user.user1_profile.role = GENERAL_USER
            user.user1_profile.save()
            
        return user