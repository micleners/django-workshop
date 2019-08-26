from rest_framework import viewsets
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Event, Location
from .serializers import UserSerializer, EventSerializer, LocationSerializer
from rest_framework import serializers
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.http import HttpResponseRedirect

class EventCreateView(CreateView):
    template_name = "events/add.html"
    model = Event
    fields = ("title", "presenter", "description", "location", "time")

def createTemplateView(request):
    if request.POST["presenter"]:
        presenter = get_user_model().objects.filter(pk=request.POST["presenter"])[0]
    else:
        presenter = request.user
    event = Event.objects.create(
        title=request.POST["title"],
        presenter=presenter,
        description=request.POST["description"],
        location=request.POST["location"],
    )
    return HttpResponseRedirect(
        reverse("events:list")
    )
    # want an extra challenge? Create a detail view
    # and see if you can get this redirect response to work:
    # return HttpResponseRedirect(
    #     reverse("events:details", kwargs={"event_id": event.pk})
    # )

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy("events:list")

    def get_object(self, queryset=None):
        pk = self.request.POST["pk"]
        return self.get_queryset().filter(pk=pk).get()

def listTemplateView(request):
    events = Event.objects.all()
    return render(request, "events/index.html", {"events": events})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    resource_name = 'events'
    queryset = Event.objects.all().order_by('-time')
    serializer_class = EventSerializer

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    resource_name = 'locations'
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer
