from django import forms
import datetime 
from .models import Booking , RageRoomSession
from django.views.decorators.http import require_POST
import datetime

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = RageRoomSession
        fields=['title','description','date','start_time','end_time','capacity','image']
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
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'capacity', 'image']
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

class EventDeleteForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean_event_id(self):
        event_id = self.cleaned_data.get('event_id')
        try:
            RageRoomSession.objects.get(id=event_id)
        except RageRoomSession.DoesNotExist:
            raise forms.ValidationError('The specified event does not exist')
        return event_id
