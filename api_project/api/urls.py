# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList # Import BookList if you still want to keep it

# Create a router instance
router = DefaultRouter()

# Register your BookViewSet with the router
# The 'r' before 'books_all' indicates a raw string, useful for regex
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: Keep the BookList if you want a separate /api/books/ endpoint for listing
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]