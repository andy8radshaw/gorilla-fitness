from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=50)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(
        'jwt_auth.User',
        related_name='events_joined',
        blank=True
    )
    related_group = models.ForeignKey(
        'workout_groups.WorkoutGroup',
        related_name='related_events',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        related_name='created_events',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}'



