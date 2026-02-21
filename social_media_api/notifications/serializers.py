from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_type = serializers.CharField(source='target_content_type.model', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'actor', 'actor_username', 'verb', 'target_type', 'timestamp', 'is_read']