# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, 
from .models import Library # Import Library for the class-based view
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import user_passes_test

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # The variable name to use in the template

# Custom Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:login') # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom Login View (inherits from Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True # Redirect logged-in users away from the login page

# Custom Logout View (inherits from Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html' # This template is shown after logout
    next_page = reverse_lazy('relationship_app:login') # Redirect to login page after logout

# --- New: Role-Based Access Control Helper Functions ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- New: Role-Based Views ---

@user_passes_test(is_admin, login_url=reverse_lazy('relationship_app:login'))
def admin_view(request):
    # This view is only accessible to users with 'Admin' role
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@user_passes_test(is_librarian, login_url=reverse_lazy('relationship_app:login'))
def librarian_view(request):
    # This view is only accessible to users with 'Librarian' role
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member, login_url=reverse_lazy('relationship_app:login'))
def member_view(request):
    # This view is only accessible to users with 'Member' role
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})

    # Optional: If you need to add extra context or do more complex things
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # You can add more context here if needed
    #     return context