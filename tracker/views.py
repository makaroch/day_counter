from django.shortcuts import render
from .models import Event

def index(request):
    event = Event.objects.all().order_by("name")
    return render(request, 'tracker/index.html', {'events': event})
