from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to list all books or create a new book.

    - GET /books/: Returns a list of all books.
      - Permissions: Allows read access to any user (authenticated or unauthenticated).
                     Requires authentication for creating new books.
    - POST /books/: Creates a new book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer (e.g., publication_year not in future).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read for anyone, write for authenticated

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single book by its ID.

    - GET /books/<int:pk>/: Retrieves details of a specific book.
      - Permissions: Allows read access to any user.
    - PUT /books/<int:pk>/: Updates an existing book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer.
    - PATCH /books/<int:pk>/: Partially updates an existing book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer.
    - DELETE /books/<int:pk>/: Deletes a specific book.
      - Permissions: Requires authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can retrieve, update, or delete

# Optional: Add views for Author if needed, similar to Book
class AuthorListCreateView(generics.ListCreateAPIView):
    """
    API view to list all authors or create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single author by their ID.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

