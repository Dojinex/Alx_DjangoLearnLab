from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models import User as CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


# -------------------------
# Register User
# -------------------------
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Get token for user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": serializer.data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)


# -------------------------
# Login User
# -------------------------
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get user from validated_data
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)


# -------------------------
# Profile View
# -------------------------
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# -------------------------
# Follow User View
# -------------------------
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": "User followed successfully"}, status=status.HTTP_200_OK)


# -------------------------
# Unfollow User View
# -------------------------
class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "User unfollowed successfully"}, status=status.HTTP_200_OK)