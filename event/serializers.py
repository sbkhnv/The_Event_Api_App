from rest_framework import serializers
from .models import Schedule,Speakers,Sponsors,Hotels,Tickets,Gallery


class SpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ("image","first_name","last_name","Speciality")

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("images")

class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = ("images")

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("image","first_name","last_name")

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = ("image","name","description")

class TicketsSerializer(serializers.ModelSerializer):
    speakers = SponsorsSerializer(read_only=True)
    class Meta:
        model = Tickets
        fields = ("__all__")



