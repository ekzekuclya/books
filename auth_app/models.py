from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SignupInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    info = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)
