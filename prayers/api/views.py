from musicapp.models import Prayers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from prayers.models import CustomPrayers, PrayerRequested
from .serializers import CustomPrayerSerializer, PrayersRequestedSerializers


class CustomPrayersCreateAPIView(CreateAPIView):
    
    """   
        Create Playlist details 
    """
    serializer_class = CustomPrayerSerializer
    fields = "__all__"
    model = serializer_class.Meta.model


class CustomPrayerAPIView(ListAPIView):
    serializer_class = CustomPrayerSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class PrayersRequestedAPIView(ListAPIView):
    serializer_class = PrayersRequestedSerializers
    fields = "__all__"
    model = serializer_class.Meta.model