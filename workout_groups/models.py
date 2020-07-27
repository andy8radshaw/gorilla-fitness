from django.db import models

class WorkoutGroup(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='created_workout_groups',
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        'jwt_auth.User',
        related_name='workout_groups_joined',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
