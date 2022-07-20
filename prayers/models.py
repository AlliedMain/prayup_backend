from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomPrayers(models.Model):
    prayer = models.TextField(max_length=1250, null=True)
    requested_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    request_time = models.DateTimeField()

    def __str__(self):
        return self.requested_user

    class Meta:
        verbose_name_plural = "CustomPrayers"