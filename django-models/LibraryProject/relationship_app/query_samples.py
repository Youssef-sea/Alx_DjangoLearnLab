import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Clear existing data for a clean run (optional, for testing)
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create sample data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Agatha Christie")

    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    book5 = Book.objects.create(title="And Then There Were None", author=author3)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2, book3)

    library2 = Library.objects.create(name="Community Library")
    library2.books.add(book4, book5)

    librarian1 = Librarian.objects.create(name="Alice Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Johnson", library=library2)


    print("--- Query Samples ---")

    # 1. Query all books by a specific author.
    print("\n1. Books by J.K. Rowling:")
    jk_rowling_books = Book.objects.filter(author__name="J.K. Rowling")
    for book in jk_rowling_books:
        print(f"  - {book.title}")

    # 2. List all books in a library.
    print("\n2. Books in a specified Library:")
    # Using a variable for the library name
    library_name = "Central Library"
    try:
        specific_library = Library.objects.get(name=library_name)
        for book in specific_library.books.all():
            print(f"  - {book.title}")
    except Library.DoesNotExist:
        print(f"  Library '{library_name}' not found.")


    # 3. Retrieve the librarian for a library.
    print("\n3. Librarian for Community Library:")
    community_library = Library.objects.get(name="Community Library")
    librarian = Librarian.objects.get(library=community_library)
    print(f"  - {librarian.name}")

if __name__ == '__main__':
    run_queries()