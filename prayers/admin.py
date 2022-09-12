from django.contrib import admin
from .models import CustomPrayers,PrayerRequested

# Register your models here.
admin.site.register(CustomPrayers)
admin.site.register(PrayerRequested) 