from django import forms
from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory

from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
