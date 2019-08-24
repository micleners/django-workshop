from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    workplace = models.CharField(max_length=256, blank=True, null=True)
    contributor = models.BooleanField(blank=True, null=True)
