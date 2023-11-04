from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    fullname = models.CharField(max_length=150)
    born_date = models.CharField(max_length=15)
    born_location = models.CharField(max_length=150)
    description = models.TextField()


class Qoutes(models.Model):
    author = models.ForeignKey(
        Authors, on_delete=models.CASCADE, default=None, null=True
    )
    quote = models.TextField()
