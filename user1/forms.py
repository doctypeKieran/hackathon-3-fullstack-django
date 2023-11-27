from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, STAFF, GENERAL_USER

class StaffUserCreationForm(UserCreationForm):
    badge_number=forms.CharField(max_length=10,required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.role = STAFF
            if self.cleaned_data.get("badge_number"):
                user.profile.badge_number = self.cleaned_data["badge_number"]
            user.profile.save()
        return user
class GeneralUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=UserCreationForm.Meta.fields + ('email',)
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.profile.role = GENERAL_USER
            user.profile.save()
        return user