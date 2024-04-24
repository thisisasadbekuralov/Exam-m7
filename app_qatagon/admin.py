from django.contrib import admin

from .models import Victim, Event

admin.site.register(Victim)
admin.site.register(Event)


class VictimAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')