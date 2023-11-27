from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from .models import STAFF, RageRoomSession 



@login_required
def create_event(request):
    #only staff can view this 
    session = RageRoomSession()
    session.facilitator = request.user.user1_profile
    if not request.user.user1_profile.role == STAFF:
        return redirect('some_error_page')

    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save(commit=False)
            session.facilitator = request.user.user1_profile
            session.save()
            return redirect('/')

    else:
        form = EventCreationForm()
    return render(request, 'event/create-event.html',{'form':form})

@login_required
def join_event(request):
    if request.method == 'POST':
        form = EventJoinForm(request.POST)
        if form.is_valid:
            booking = form.save(commit=False)
            booking.participant = request.user.userprofile
            booking.save()
            return redirect('event-list')
    else:
        form=EventJoinForm()
    
    return render(request, 'event-list.html', {'form':form})

# Create your views here.

def view_events(request):
    # Filter when approved field gets added to model
    events = RageRoomSession.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'event/event-list.html', context)