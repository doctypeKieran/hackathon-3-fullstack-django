from django import forms
import datetime 
from .models import Booking , RageRoomSession
from django.views.decorators.http import require_POST
import datetime

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = RageRoomSession
        fields=['title','description','date','start_time','end_time','capacity','featured_image']
        widgets = {
            'date':forms.DateInput(attrs={'type': 'date'}
            ),
            'start_time':forms.TimeInput(attrs={'type':'time'}),
            'end_time':forms.TimeInput(attrs={'type':'time'}),
            'description':forms.Textarea(attrs={'rows':4}),

        }

class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = RageRoomSession
        exclude = ['capacity'] 
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'capacity', 'featured_image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    def clean_capacity(self):
        capacity = self.cleaned_data.get('capacity')
        if capacity != 10:
            raise forms.ValidationError('Capacity must remain at 10 to update the event. ')


