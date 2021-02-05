from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    sex = models.CharField(max_length=20, default='Male')
