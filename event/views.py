from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from .models import STAFF 



@login_required
def create_event(request):
    #only staff can view this 
    if not request.user.userprofile.role == STAFF:
        return redirect('some_error_page')

    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.facilitator = request.user.userprofile
            event.save()
            return redirect('event-list.html')

    else:
        form = EventCreationForm()
    return request(request, 'create-event.html',{'form':form})

@login_required
def join_event(request):
    if request.method == 'POST':
        form = EventJoinForm(request.POST)
        if form.is_valid:
            booking = form.save(commit=False)
            booking.participant = request.user.userprofile
            booking.save()
            return redirect('event-list.html')
    else:
        form=EventJoinForm()
    
    return render(request, 'join-event.html', {'form':form})

# Create your views here.
