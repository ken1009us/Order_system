from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField()
    sex = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = "user"
