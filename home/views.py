from django.shortcuts import render

from event.models import RageRoomSession

# Create your views here.
def home_page(request):

    return render(
        request,
        "home/home.html",
        {
            
        }
    )

def home(request):
    events = RageRoomSession.objects.all()  # Retrieves all events, adjust the query as needed
    context = {
        'events': events, }
    return render(request, 'home.html', context)