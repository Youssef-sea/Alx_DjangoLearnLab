# bookshelf/models.py

from django.db import models

class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        title (CharField): The title of the book, with a maximum length of 200 characters.
        author (CharField): The author of the book, with a maximum length of 100 characters.
        publication_year (IntegerField): The year the book was published.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        String representation of the Book instance.
        Returns the title and author of the book.
        """
        return f"{self.title} by {self.author}"

    class Meta:
        """
        Meta options for the Book model.
        Orders books by title by default.
        """
        ordering = ['title']
