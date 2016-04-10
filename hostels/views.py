from django.shortcuts import render
from django.http import HttpResponse
from .models import Hostel

def menu(request):
    a = Hostel.objects.all()
    context = {'hostels':a}
    return render(request, 'hostels/menu.html',context)
