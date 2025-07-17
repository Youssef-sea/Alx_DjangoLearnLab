# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

app_name = 'relationship_app' # Namespace for the app's URLs

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
 # Authentication views  
    path('register/', register, name='register'), # Already uses views.register
    path('login/',
         LoginView.as_view(template_name='relationship_app/login.html'), # <--- LoginView directly
         name='login'),
    path('logout/',
         LogoutView.as_view(next_page=reverse_lazy('relationship_app:login'), template_name='relationship_app/logout.html'), # <--- LogoutView directly
         name='logout'),
]