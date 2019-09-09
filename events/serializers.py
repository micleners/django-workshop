from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Event
from rest_framework import serializers


# serializers to convert from Django model objects to JSON
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'groups')

# or specify all fields
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'