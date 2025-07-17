# relationship_app/urls.py
from django.urls import path
from .views import book_list, LibraryDetailView

app_name = 'relationship_app' # Namespace for the app's URLs

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]