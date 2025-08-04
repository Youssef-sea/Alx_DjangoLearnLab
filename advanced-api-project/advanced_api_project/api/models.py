# api/models.py

from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    This model stores basic information about an author, specifically their name.
    It serves as the 'one' side of a one-to-many relationship with the Book model,
    meaning one author can write multiple books.
    """
    name = models.CharField(max_length=255, help_text="The full name of the author.")

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.
    This model stores details about a book, including its title, publication year,
    and a foreign key link to the Author model. This establishes a one-to-many
    relationship where each book is written by exactly one author.
    """
    title = models.CharField(max_length=255, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, # If an author is deleted, all their books are also deleted.
        related_name='books',     # Allows accessing books from an Author instance (e.g., author.books.all())
        help_text="The author of this book."
    )

    class Meta:
        # Ensures that a combination of title and author is unique, preventing duplicate books by the same author.
        unique_together = ('title', 'author')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

