from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
