from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Event, Location
from rest_framework import serializers


# or specify all fields
class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

# serializers to convert from Django model objects to JSON
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # events = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='event-detail'
    # )
    class Meta:
        model = get_user_model()
        # fields = ('url', 'first_name', 'last_name', 'username', 'email', 'events')
        fields = ('url', 'first_name', 'last_name', 'username', 'email')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='event-detail'
    )
    class Meta:
        model = Location
        fields = ('url', 'name', 'company', 'address', 'contact_primary', 'contact_secondary', 'description', 'events')

