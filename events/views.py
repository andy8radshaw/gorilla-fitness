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
        serialized_events = EventSerializer(events, many=True)
        return Response(serialized_events.data, status=status.HTTP_200_OK)

    # * Create a new event
    def post(self, request):
        request.data['owner'] = request.user.id
        new_event = EventSerializer(data=request.data)
        if new_event.is_valid():
            new_event.save()
            return Response(new_event.data, status=status.HTTP_201_CREATED)
        return Response(new_event.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class EventDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get_event(self, pk):
        try: 
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise NotFound()

    def is_event_owner(self, event, user):
        if event.owner.id != user.id:
            raise PermissionDenied()

    def get(self, _request, pk):
        event = self.get_event(pk)
        serialized_event = PopulatedEventSerializer(event)
        return Response(serialized_event.data)

    def put(self, request, pk):
        event_to_update = self.get_event(pk)
        updated_event = EventSerializer(event_to_update, data=request.data)
        if updated_event.is_valid():
            updated_event.save()
            return Response(updated_event.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_event.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        event_to_delete = self.get_event(pk)
        self.is_event_owner(event_to_delete, request.user)
        event_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
