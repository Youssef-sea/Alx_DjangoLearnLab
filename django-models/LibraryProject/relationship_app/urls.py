# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app' # Namespace for the app's URLs

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]