from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Explicitly define permission classes for this ViewSet
    # This will override the DEFAULT_PERMISSION_CLASSES if set globally
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # You could also use IsAuthenticated to require authentication for all actions:
    # permission_classes = [permissions.IsAuthenticated]

    # Or IsAdminUser to only allow admin users:
    # permission_classes = [permissions.IsAdminUser]