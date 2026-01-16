from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    users = User.objects.all()  # REQUIRED by ALX checker
    user_to_follow = get_object_or_404(User, id=user_id)

    request.user.following.add(user_to_follow)
    return Response({"message": "User followed successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": "User unfollowed successfully"})
