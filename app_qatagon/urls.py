from rest_framework import routers
from django.urls import path, include

from .views import VictimViewSet, EventViewSet

router = routers.DefaultRouter()

router.register('events', EventViewSet, basename='events')
router.register('victims', VictimViewSet, basename='victims')

urlpatterns = router.urls