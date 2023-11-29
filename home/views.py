from django.shortcuts import render

from event.models import RageRoomSession

# Create your views here.


def home_page(request):
    events = RageRoomSession.objects.all()  #
    context = {
        'events': events, }

    return render(
        request,
        "home/home.html", context
    )
