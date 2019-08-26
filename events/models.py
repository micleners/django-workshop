from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Location(models.Model):
    # Only required field is title
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    contact_primary = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name="contact_primary"
    )
    contact_secondary = models.ForeignKey(
      get_user_model(),
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name="contact_secondary"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)

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
    location = models.ForeignKey(
      Location,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name='events'
    )
    # location = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
