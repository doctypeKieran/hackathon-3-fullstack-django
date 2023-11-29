from django.shortcuts import render, redirect
from .forms import StaffUserCreationForm, GeneralUserCreationForm


def register(request,user_type):
    if user_type == 'staff':
        form_class = StaffUserCreationForm
    else:
        form_class =GeneralUserCreationForm

    if request.method =='POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = form_class()
    return render(request,'user1/registration.html',{'form':form})
# Create your views here.
