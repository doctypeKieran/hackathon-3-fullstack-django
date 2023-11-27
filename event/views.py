from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm , EventJoinForm
from .models import STAFF, RageRoomSession ,Booking
from django.http import JsonResponse
from django.contrib import messages



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
def join_event(request, event_id):
    session = get_object_or_404(RageRoomSession, pk=event_id)
    if request.method == 'POST':
        existing_booking = Booking.objects.filter(participant=request.user.user1_profile, session=session, approved=False)
        if existing_booking:
            messages.success(request, 'Your request to join has been sent.')
            return redirect('event-list')
        else:
            Booking.objects.create(participant=request.user.user1_profile,session=session, approved=False)
            messages.success(request,'Your request to join has been sent')
            return redirect('event-list')
    else:
        return redirect('event-list')


# Create your views here.

def view_events(request):
    # Filter when approved field gets added to model
    events = RageRoomSession.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'event/event-list.html', context)

def manage_bookings(request):
    if request.user.user1_profile.role == STAFF:
        pending_bookings = Booking.objects.filter(approved=False)
        return render(request, 'manage_bookings.html',{'pending_bookings':pending_bookings})
    else:
        return redirect('some_error_page')
def approve_booking(request,booking_id):
    if request.user.user1_profile != STAFF:
        return redirect('some_error_page')
    booking = get_object_or_404(Booking, id=booking_id)
    action = request.POST.get('action')
