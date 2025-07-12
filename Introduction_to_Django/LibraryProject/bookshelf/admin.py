# bookshelf/admin.py

from django.contrib import admin
from .models import Book # Import the Book model from the current app's models.py

# Register your models here.

# Option 1: Simple registration
# admin.site.register(Book)

# Option 2: Register with a custom ModelAdmin for enhanced features
@admin.register(Book) # This decorator registers the Book model with the admin site
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model in the Django admin.
    """
    # Fields to display in the list view of the admin interface
    list_display = ('title', 'author', 'publication_year')

    # Fields to use for filtering in the right sidebar of the admin interface
    list_filter = ('publication_year', 'author')

    # Fields to enable search functionality in the admin interface
    search_fields = ('title', 'author')

    # Fields to make clickable links to the detail view
    list_display_links = ('title',)

    # Number of items to display per page in the list view
    list_per_page = 25

    # Order of fields in the add/change form (optional, useful for complex models)
    # fields = ('title', 'author', 'publication_year')

    # Grouping fields into fieldsets (optional, for better organization in forms)
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'author')
    #     }),
    #     ('Publication Info', {
    #         'fields': ('publication_year',),
    #         'classes': ('collapse',), # Makes this section collapsible
    #     }),
    # )
