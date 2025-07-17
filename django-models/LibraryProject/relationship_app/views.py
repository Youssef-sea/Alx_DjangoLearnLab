# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, 
from .models import Library # Import Library for the class-based view

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

    # Optional: If you need to add extra context or do more complex things
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # You can add more context here if needed
    #     return context