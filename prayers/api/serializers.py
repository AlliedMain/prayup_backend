from rest_framework import serializers

from prayers.models import CustomPrayers, PrayerRequested

class CustomPrayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomPrayers
        fields = "__all__"    
        
class PrayersRequestedSerializers(serializers.ModelSerializer):


    class Meta:
        model = PrayerRequested
        fields = "__all__"