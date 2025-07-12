### Retrieve Operation 
Command:
from bookshelf.models import Book
book = Book.objects.get(title="1984") # Ou utilisez l'ID si vous l'avez : book = Book.objects.get(id=1)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"Book ID: {book.id}")