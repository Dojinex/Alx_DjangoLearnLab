from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer




class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return notifications for the logged-in user
        return self.request.user.notifications.all()