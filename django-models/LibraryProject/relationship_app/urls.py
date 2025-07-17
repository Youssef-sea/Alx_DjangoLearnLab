# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book 

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
         LogoutView.as_view(template_name='relationship_app/logout.html'), # <--- LogoutView directly
         name='logout'),

# Role-based views
    path('admin_dashboard/', admin_view, name='admin_view'),       # URL for Admin view
    path('librarian_dashboard/', librarian_view, name='librarian_view'), # URL for Librarian view
    path('member_dashboard/', member_view, name='member_view'),  
 
# NEW: URLs for custom permission-based book actions
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/edit/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/delete/', delete_book, name='delete_book'),

]