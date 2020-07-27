# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import WorkoutGroup
from .serializers import WorkoutGroupSerializer, PopulatedWorkoutGroupSerializer

class WorkoutGroupListView(APIView):

    def get(self, _request):
        groups = WorkoutGroup.objects.all()
        serialized_groups = PopulatedWorkoutGroupSerializer(groups, many=True)
        return Response(serialized_groups.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        new_workout_group = WorkoutGroupSerializer(data=request.data)
        if new_workout_group.is_valid():
            new_workout_group.save()
            return Response(new_workout_group.data, status=status.HTTP_201_CREATED)
        return Response(new_workout_group.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class WorkoutGroupDetailView(APIView):

    def get_group(self, pk):
        try:
            return WorkoutGroup.objects.get(pk=pk)
        except WorkoutGroup.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        workout_group = self.get_group(pk)
        serialized_workout_group = PopulatedGroupSerializer(workout_group)
        return Response(serialized_workout_group.data)
