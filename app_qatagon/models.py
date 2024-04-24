from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Victim(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_repression = models.DateField()
    biography = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='victims_photos/', null=True, blank=True)

    def clean(self):
        super().clean()
        today = timezone.localdate()
        if self.date_of_birth > today or self.date_of_repression > today:
            raise ValidationError("Date cannot be in the future.")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Victim'
        verbose_name_plural = 'Victims'
        db_table = 'victim'


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    victims = models.ManyToManyField(Victim, related_name='events')

    def clean(self):
        super().clean()
        today = timezone.localdate()
        if self.date > today:
            raise ValidationError("Date cannot be in the future.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        db_table = 'event'
