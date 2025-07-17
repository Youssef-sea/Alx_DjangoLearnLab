# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

app_name = 'relationship_app' # Namespace for the app's URLs

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
 # Authentication views
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]