from django.shortcuts import render

from event.models import RageRoomSession

# Create your views here.
def about_page(request):
    events = RageRoomSession.objects.all()
    context = {'events': events}

    return render(request, 'about/about.html', context)

#from django.shortcuts import render

# Create your views here.
#def about_page(request):

   # return render(
   #     request,
   #     "about/about.html",
   #     {
   #         
   #     }
  #  )