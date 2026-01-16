from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User.objects.all(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": "User followed successfully"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User.objects.all(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "User unfollowed successfully"})
