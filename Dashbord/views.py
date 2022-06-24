from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

@login_required
def Dashbord(request):
    return render(request, 'Dashbord/Dashbord.html')
