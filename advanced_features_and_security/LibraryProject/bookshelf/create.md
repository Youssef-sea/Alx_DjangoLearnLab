Create Operation
Command:from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
print(book.id)
Expected Output:1984 by George Orwell
1
(Note: The id will be 1 for the first book created. Subsequent books will have incrementing IDs.)