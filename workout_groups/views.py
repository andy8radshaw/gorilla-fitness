# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import WorkoutGroup
from .serializers import WorkoutGroupSerializer, PopulatedWorkoutGroupSerializer

User = get_user_model()

class WorkoutGroupListView(APIView):

    permission_classes = (IsAuthenticated, )

    # * Gets all workout groups
    def get(self, _request):
        groups = WorkoutGroup.objects.all()
        serialized_groups = PopulatedWorkoutGroupSerializer(groups, many=True)
        return Response(serialized_groups.data, status=status.HTTP_200_OK)

    # * Creates a new workout group
    def post(self, request):
        if request.user.is_admin:
            request.data['owner'] = request.user.id
            new_workout_group = WorkoutGroupSerializer(data=request.data)
            if new_workout_group.is_valid():
                new_workout_group.save()
                return Response(new_workout_group.data, status=status.HTTP_201_CREATED)
            return Response(new_workout_group.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

class WorkoutGroupDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    # * Checks if workout group is real
    def get_group(self, pk):
        try:
            return WorkoutGroup.objects.get(pk=pk)
        except WorkoutGroup.DoesNotExist:
            raise NotFound()

    def is_group_owner(self, group, user):
        if group.owner.id != user.id:
            raise PermissionDenied()

    # * Gets single workout group
    def get(self, _request, pk):
        workout_group = self.get_group(pk)
        serialized_workout_group = PopulatedWorkoutGroupSerializer(workout_group)
        return Response(serialized_workout_group.data)

    # * Updates a workout group
    def put(self, request, pk):
        workout_group_to_update = self.get_group(pk)
        updated_workout_group = WorkoutGroupSerializer(workout_group_to_update, data=request.data)
        if updated_workout_group.is_valid():
            updated_workout_group.save()
            return Response(updated_workout_group.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_workout_group.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # * Deletes a workout group
    def delete(self, request, pk):
        workout_group_to_delete = self.get_group(pk)
        self.is_group_owner(workout_group_to_delete, request.user)
        workout_group_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
