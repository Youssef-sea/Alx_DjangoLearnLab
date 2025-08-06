# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework 
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListView(generics.ListAPIView):
    """
    API view to list all books.

    - GET /books/: Returns a list of all books.
      - Permissions: Allows read access to any user (authenticated or unauthenticated).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read for anyone

    # --- Filtering Configuration ---
    # Specifies the filter backends to use for this view.
    filter_backends = [
        rest_framework,   # For exact/range filtering
        filters.SearchFilter,         # For text searching
        filters.OrderingFilter        # For sorting results
    ]

    # Defines the fields available for rest_framework.
    # 'author__name' allows filtering by the author's name through the foreign key.
    filterset_fields = ['title', 'author__name', 'publication_year']

    # --- Search Configuration ---
    # Defines the fields that SearchFilter will search within.
    # '^' starts-with search, '=' exact match, '@' full-text search, '$' regex search.
    # No prefix implies case-insensitive partial match.
    search_fields = ['title', 'author__name']

    # --- Ordering Configuration ---
    # Defines the fields by which the results can be ordered.
    # Users can specify ordering like '?ordering=title' or '?ordering=-publication_year'.
    ordering_fields = ['title', 'publication_year']
    ordering = ['title'] # Default ordering if none is specified in the request


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a single book by its ID.

    - GET /books/<int:pk>/: Retrieves details of a specific book.
      - Permissions: Allows read access to any user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read for anyone

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.

    - POST /books/create/: Creates a new book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer (e.g., publication_year not in future).
    """
    queryset = Book.objects.all() # Although not strictly needed for CreateAPIView, good practice
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book by its ID.

    - PUT /books/<int:pk>/update/: Fully updates an existing book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer.
    - PATCH /books/<int:pk>/update/: Partially updates an existing book.
      - Permissions: Requires authenticated users.
      - Data Validation: Handled by BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a specific book by its ID.

    - DELETE /books/<int:pk>/delete/: Deletes a specific book.
      - Permissions: Requires authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer # Serializer is still required by DestroyAPIView
    permission_classes = [IsAuthenticated] # Only authenticated users can delete

# Optional: Add views for Author if needed, similar to Book
class AuthorListView(generics.ListAPIView):
    """
    API view to list all authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve details of a single author by their ID.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AuthorCreateView(generics.CreateAPIView):
    """
    API view to create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class AuthorUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing author by their ID.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

class AuthorDeleteView(generics.DestroyAPIView):
    """
    API view to delete a specific author by their ID.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

