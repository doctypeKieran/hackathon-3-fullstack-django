from django import forms
import datetime 
from .models import Booking , RageRoomSession

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
class EventJoinForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=RageRoomSession.objects.filter(date__gte=datetime.date.today()), empty_label="Select Event")
    class Meta:
        model = Booking
        fields = ['event']