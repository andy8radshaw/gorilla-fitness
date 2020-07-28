# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import Event
from .serializers import EventSerializer, PopulatedEventSerializer

User = get_user_model()

class EventListView(APIView):

    permission_classes = (IsAuthenticated, )

    # * Gets all events
    def get(self, _request):
        events = Event.objects.all()
        serialized_events = PopulatedEventSerializer(events, many=True)
        return Response(serialized_events.data, status=status.HTTP_200_OK)