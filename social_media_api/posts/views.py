from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Custom permission: Only owner can edit/delete
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for everyone.
    Allow write only for the owner.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE methods (GET, HEAD, OPTIONS) allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check ownership
        return obj.author == request.user


# ========================
# POST VIEWSET
# ========================
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set logged-in user as author
        serializer.save(author=self.request.user)


# ========================
# COMMENT VIEWSET
# ========================
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
