# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles the conversion of Book model instances to JSON
    representations and vice-versa. It includes custom validation to ensure
    that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        # 'author' field is included here, but for nested serialization
        # in AuthorSerializer, we'll use a specific representation.

    def validate_publication_year(self, value):
        """
        Custom validation for the publication_year field.
        Ensures that the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer handles the conversion of Author model instances to JSON
    representations. It demonstrates nested serialization by including
    a representation of all books written by the author.

    The 'books' field uses BookSerializer(many=True) to serialize a list of
    related Book objects. The 'read_only=True' ensures that books cannot be
    created or updated directly through the AuthorSerializer, but are
    included in the output when an Author instance is retrieved.
    """
    # Nested serializer to display all books related to an author.
    # 'many=True' indicates that there can be multiple books.
    # 'read_only=True' means this field is only for output and cannot be
    # used for creating or updating books via the AuthorSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] # Include 'books' to show nested relationship

