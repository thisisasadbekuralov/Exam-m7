from rest_framework import viewsets

from .models import Victim, Event
from .serializers import VictimSerializer, EventSerializer
from .filters import VictimFilter, EventFilter
from .permissions import Permissions


class VictimViewSet(viewsets.ModelViewSet):
    queryset = Victim.objects.all()
    serializer_class = VictimSerializer
    permission_classes = [Permissions]
    filterset_class = VictimFilter


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [Permissions]
    filterset_class = EventFilter
