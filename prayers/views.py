from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *



# Create your views here.

@login_required
def customprayers(request):
    custom_prayer= CustomPrayers.objects.all()
    context = {
        'prayers': custom_prayer
    }
    return render(request, 'musicapp/prayers.html', context=context)




