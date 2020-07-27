from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import WorkoutGroup

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class WorkoutGroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WorkoutGroup
        fields = '__all__'

class PopulatedWorkoutGroupSerializer(WorkoutGroupSerializer):
    owner = UserSerializer()