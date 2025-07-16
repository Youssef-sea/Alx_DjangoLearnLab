### Delete Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Utilisez le titre mis à jour
book_title = book.title
book.delete()
print(f"Deleted book: {book_title}")
# Confirmer la suppression en essayant de récupérer tous les livres
all_books = Book.objects.all()
print(f"Number of books remaining: {all_books.count()}")

Expected Output:

Deleted book: Nineteen Eighty-Four
Number of books remaining: 0
