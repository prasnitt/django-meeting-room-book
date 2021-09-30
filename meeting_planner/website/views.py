from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",context={
        "message" : "This is sent from view to template.",
        "num_meetings": Meeting.objects.count()
    })


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("Hey Prashant here. I am learning django via Pluralsight")
