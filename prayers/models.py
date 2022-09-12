from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustomPrayers(models.Model):
    prayer = models.TextField(null=True)
    # requested_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # request_time = models.DateField(blank=True)
    user = models.EmailField(blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "CustomPrayers"



class PrayerRequested(models.Model):

    Language_Choice = (
              
              ('English', 'English'),
          )

    prayer_name = models.CharField(max_length=200)
    prayer_album = models.CharField(max_length=200)
    prayer_language = models.CharField(max_length=20,choices=Language_Choice,default='English')
    prayer_img = models.FileField(blank=True)
    year = models.IntegerField(blank=True)
    # singer = models.CharField(max_length=200)
    song_file = models.FileField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "PrayersRequested"