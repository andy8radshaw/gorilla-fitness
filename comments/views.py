# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .models import Comment
from .serializers import CommentSerializer, PopulatedCommentSerializer

User = get_user_model()

class CommentListView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        comments = Comment.objects.all()
        serialized_comments = CommentSerializer(comments, many=True)
        return Response(serialized_comments.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        new_comment = CommentSerializer(data=request.data)
        if new_comment.is_valid():
            new_comment.save()
            return Response(new_comment.data, status=status.HTTP_201_CREATED)
        return Response(new_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound()

    def is_comment_owner(self, comment, user):
        if comment.owner.id != user.id:
            raise PermissionDenied()

    def get(self, _request, pk):
        comment = self.get_comment(pk)
        serialized_comment = CommentSerializer(comment)
        return Response(serialized_comment.data)

    def put(self, request, pk):
        comment_to_update = self.get_comment(pk)
        self.is_comment_owner(comment_to_update, request.user)
        request.data['owner'] = request.user.id
        updated_comment = CommentSerializer(comment_to_update, data=request.data)
        if updated_comment.is_valid():
            updated_comment.save()
            return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        comment_to_delete = self.get_comment(pk)
        self.is_comment_owner(comment_to_delete, request.user)
        comment_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
