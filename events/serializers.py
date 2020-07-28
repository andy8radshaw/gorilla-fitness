from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Event
from workout_groups.serializers import WorkoutGroupSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

class PopulatedEventSerializer(EventSerializer):
    attendees = UserSerializer(many=True)
    related_group = WorkoutGroupSerializer()