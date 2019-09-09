from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# basic information for our events
class Event(models.Model):
    # Only required field is title
    title = models.CharField(max_length=256)
    presenter = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
    )
    # Default time is now if not provided
    time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)