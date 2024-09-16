from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_type_choices = [('PR', 'Personal'), ('ORG', 'Organization')]
    profile_type = models.CharField(max_length=3, choices=profile_type_choices)