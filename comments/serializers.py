from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Comment
from events.models import Event
from workout_groups.models import WorkoutGroup

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name')


class WorkoutGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutGroup
        fields = ('id', 'name')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    related_event = EventSerializer()
    related_group = WorkoutGroupSerializer()
