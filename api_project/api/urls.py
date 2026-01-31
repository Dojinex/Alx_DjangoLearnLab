from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


# Create a router and register our viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the simple list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes registered with the router
    path('', include(router.urls)),
]