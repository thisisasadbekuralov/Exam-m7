from rest_framework import serializers

from .models import Victim, Event


class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
