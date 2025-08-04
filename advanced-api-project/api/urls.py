# api/urls.py

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
)

urlpatterns = [
    # URLs for Book model
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'), # Explicit create path
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'), # Explicit update path
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), # Explicit delete path

    # Optional: URLs for Author model
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]

