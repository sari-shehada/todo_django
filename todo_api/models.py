import uuid
from django.db import models

# Create your models here.


class AppUser(models.Model):
    id = models.CharField(
        max_length=255, primary_key=True, default=uuid.uuid4)
    userName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class TODO(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=500)
    isFinished = models.BooleanField()
    postedBy = models.ForeignKey(AppUser, on_delete=models.CASCADE)
