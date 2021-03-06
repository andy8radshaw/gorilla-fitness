from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.apps import apps 


User = get_user_model()
WorkoutGroup = apps.get_model('workout_groups', 'WorkoutGroup')

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise ValidationError({'password': err.messages})
        data['password'] = make_password(password)
        return data


    class Meta:
        model = User
        fields = '__all__'

class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ('password', )

class WorkoutGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutGroup
        fields = ('id', 'name')



class PopulatedUserSerializer(UserSerializer):
    created_workout_groups = WorkoutGroupSerializer(many=True)
    workout_groups_joined = WorkoutGroupSerializer(many=True)