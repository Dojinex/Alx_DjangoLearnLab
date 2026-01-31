from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use our serializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on Books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
