from rest_framework import viewsets
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Event
from .serializers import UserSerializer, EventSerializer
from rest_framework import serializers
from django.shortcuts import render  # new


def listTemplateView(request):  # new
    events = Event.objects.all()  # new
    return render(request, "events/index.html", {"events": events})  # new


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = get_user_model().objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    resource_name = "events"
    queryset = Event.objects.all().order_by("-time")
    serializer_class = EventSerializer
