from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm ,UpdateEventForm,EventDeleteForm
from .models import STAFF, RageRoomSession ,Booking
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST



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


# Create your views here.

def view_events(request):
    # Filter when approved field gets added to model
    events = RageRoomSession.objects.all()
    user_bookings = Booking.objects.filter(participant=request.user.user1_profile).values_list('session',flat=True) if request.user.is_authenticated else []
    context = {
        'events': events,
        'user_bookings': user_bookings,
    }

    return render(request, 'event/event-list.html', context)
def join_event(request,event_id):
    if request.method == 'POST':
        event = get_object_or_404(RageRoomSession, id=event_id)
        Booking.objects.create(session=event, participant=request.user.user1_profile)
    return redirect('event-list')
def manage_bookings(request):
    if request.user.user1_profile.role == STAFF:
        pending_bookings = Booking.objects.filter(approved=False)
        return render(request, 'event/manage_bookings.html', {'pending_bookings': pending_bookings})
    else:
        return redirect('some_error_page')

def approve_booking(request,booking_id):
    if request.user.user1_profile != 'STAFF':
        messages.error(request, "You do not have permission to perform this action.")   

    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'approve':
            booking.approve_booking(request.user)

        elif action =='decline':
            booking.delete()

    return redirect('manage_bookings')

def user_bookings(request):
    user_profile=request.user.user1_profile
    approve_bookings=Booking.objects.filter(participant=user_profile,approved=True)
    pending_bookings=Booking.objects.filter(participant=user_profile,approved=False)
    context = {
        'approved_bookings': approve_bookings,
        'pending_bookings': pending_bookings,
    }
    return render(request, 'event/user_bookings.html', context)

def update_event(request, event_id):
    event = get_object_or_404(RageRoomSession, id=event_id)

    if not request.user.user1_profile.role == 'STAFF':
        return redirect('some_error_page')

    if request.method == 'POST':
        form = UpdateEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = UpdateEventForm(instance=event)

    return render(request, 'event/update_event.html', {'form': form})


@require_POST
def delete_event(request):
    event_id = request.POST.get('event_id')
    event = get_object_or_404(RageRoomSession, id=event_id)

    if request.user.user1_profile.role == 'STAFF':
        return redirect('some_error_page')
    event.delete()
    return redirect('event/events_list')
