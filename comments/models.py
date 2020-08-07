from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    text = models.CharField(max_length=300)
    owner = models.ForeignKey(
        User,
        related_name='created_comments',
        on_delete=models.CASCADE
    )
    related_group = models.ForeignKey(
        'workout_groups.WorkoutGroup',
        related_name='related_comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    related_event = models.ForeignKey(
        'events.Event',
        related_name='related_comments',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.owner} - {self.text}'
