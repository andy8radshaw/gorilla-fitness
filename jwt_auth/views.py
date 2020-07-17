from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from .serializers import UserSerializer, UpdateUserSerializer
User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        created_user = UserSerializer(data=request.data)
        if created_user.is_valid():
            created_user.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(created_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied()

    def post(self, request):
        email = request.data.get('email')
        password  = request.data.get('password')
        user = self.get_user(email)
        if not user.check_password(password):
            raise PermissionDenied()
        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode({
            'sub': user.id,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY)
        return Response({'token': token, 'message': f'Welcome back {user.username}'})


class ProfileListView(APIView):

    # * Can only access if logged in
    permission_classes = (IsAuthenticated, )

    # * Get all users
    def get(self, request):
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)


        
class MyProfileView(APIView):

    # * Can only access if logged in
    permission_classes = (IsAuthenticated, )


    # * Checks if user is legit
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound()

    # ! Will need to update all below later with serialized events/workouts/groups etc... --------

    # * Gets current user profile
    def get(self, request):
        user = self.get_user(username=request.user.username)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)

    # * Updates current user
    def put(self, request):
        user_to_update = self.get_user(username=request.user.username)
        updated_user = UpdateUserSerializer(user_to_update, data=request.data, context={'request': 'update'})
        if updated_user.is_valid():
            updated_user.save()
            return Response(updated_user.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    # * Deletes current user
    def delete(self, request):
        user_to_delete = self.get_user(username= request.user.username)
        user_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileDetailView(APIView):

    # * Can only access if logged in
    permission_classes = (IsAuthenticated, )

    # * Checks if user is legit
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound()

    # * Gets a selected user
    def get(self, _request, username):
        user = self.get_user(username)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
