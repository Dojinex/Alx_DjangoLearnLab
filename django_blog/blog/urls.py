from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    SearchResultsView,
    TagPostsView,
)

urlpatterns = [
    # =========================
    # AUTH ROUTES
    # =========================
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),

    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout"
    ),

    # =========================
    # POSTS CRUD
    # =========================
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # =========================
    # COMMENTS
    # =========================
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    # =========================
    # SEARCH + TAGS
    # =========================
    path("search/", SearchResultsView.as_view(), name="search"),
    path("tags/<str:tag_name>/", TagPostsView.as_view(), name="tag-posts"),
]



