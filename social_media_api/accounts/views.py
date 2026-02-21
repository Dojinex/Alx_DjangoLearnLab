from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from .models import User as CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

# Register views
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)

        return Response({
            "user": serializer.data,
            "token": token.key
        })

#Login views
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key
        })

# Profile views
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = self.get_queryset().filter(id=user_id).first()

        if not user_to_follow:
            return Response({"error": "User not found"}, status=404)

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": "User followed successfully"})


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = self.get_queryset().filter(id=user_id).first()

        if not user_to_unfollow:
            return Response({"error": "User not found"}, status=404)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": "User unfollowed successfully"})