# Generated by Django 3.0.8 on 2020-07-27 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='workout_groups_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
