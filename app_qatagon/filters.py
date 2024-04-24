from django_filters import rest_framework as filters
from .models import Victim, Event

class VictimFilter(filters.FilterSet):
    class Meta:
        model = Victim
        fields = {
            'name': ['exact', 'icontains'],
            'date_of_birth': ['exact', 'gt', 'lt'],
            'date_of_repression': ['exact', 'gt', 'lt'],
        }


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'title': ['exact', 'icontains'],
            'date': ['exact', 'gt', 'lt'],
        }