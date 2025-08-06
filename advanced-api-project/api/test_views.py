# api/test_views.py

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models import Author, Book
from datetime import date

class BookAPITests(APITestCase):
    """
    Comprehensive unit tests for the Book model API endpoints.
    Covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        """
        Set up initial data and clients for testing.
        This method runs before each test case.
        """
        # Create a regular user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user) # Create a token for the user

        # Create an admin user (optional, but good for testing different roles if needed)
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpassword')
        self.admin_token = Token.objects.create(user=self.admin_user)

        # Create an authenticated client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create an unauthenticated client
        self.unauthenticated_client = APIClient()

        # Create initial authors
        self.author1 = Author.objects.create(name="Jane Doe")
        self.author2 = Author.objects.create(name="John Smith")

        # Create initial books
        self.book1 = Book.objects.create(
            title="The First Journey",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Adventures in the North",
            publication_year=2022,
            author=self.author1
        )
        self.book3 = Book.objects.create(
            title="Mysteries of the Deep",
            publication_year=2021,
            author=self.author2
        )
        self.book4 = Book.objects.create(
            title="Another Journey",
            publication_year=2020,
            author=self.author2
        )

        # Define URLs using reverse for robustness
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    # --- Test Book List View (GET /api/books/) ---

    def test_book_list_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve the list of books.
        """
        response = self.unauthenticated_client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4) # Check if all 4 books are returned

    def test_book_list_authenticated(self):
        """
        Ensure authenticated users can retrieve the list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_book_list_filter_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(self.list_url, {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book4.title, [book['title'] for book in response.data])

    def test_book_list_filter_by_author_name(self):
        """
        Test filtering books by author name.
        """
        response = self.client.get(self.list_url, {'author__name': 'Jane Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book2.title, [book['title'] for book in response.data])

    def test_book_list_search_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url, {'search': 'Journey'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(self.book1.title, [book['title'] for book in response.data])
        self.assertIn(self.book4.title, [book['title'] for book in response.data])

    def test_book_list_search_by_author_name(self):
        """
        Test searching books by author name.
        """
        response = self.client.get(self.list_url, {'search': 'Smith'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(self.book3.title, [book['title'] for book in response.data])
        self.assertIn(self.book4.title, [book['title'] for book in response.data])

    def test_book_list_order_by_publication_year_descending(self):
        """
        Test ordering books by publication year in descending order.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2022) # book2
        self.assertEqual(response.data[1]['publication_year'], 2021) # book3
        self.assertEqual(response.data[2]['publication_year'], 2020) # book1 or book4
        self.assertEqual(response.data[3]['publication_year'], 2020) # book1 or book4

    # --- Test Book Create View (POST /api/books/create/) ---

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a new book.
        """
        data = {
            'title': 'New Book Title',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5) # 4 initial + 1 new
        self.assertEqual(response.data['title'], 'New Book Title')

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a new book.
        """
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2023,
            'author': self.author1.id
        }
        response = self.unauthenticated_client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 4) # Should not have created a book

    def test_create_book_with_future_publication_year(self):
        """
        Ensure creating a book with a future publication year fails validation.
        """
        future_year = date.today().year + 1
        data = {
            'title': 'Future Book',
            'publication_year': future_year,
            'author': self.author1.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.assertEqual(response.data['publication_year'][0], 'Publication year cannot be in the future.')
        self.assertEqual(Book.objects.count(), 4) # Should not have created a book

    def test_create_book_with_invalid_author_id(self):
        """
        Ensure creating a book with a non-existent author ID fails.
        """
        data = {
            'title': 'Book with Invalid Author',
            'publication_year': 2023,
            'author': 9999 # Non-existent author ID
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('author', response.data)
        self.assertEqual(Book.objects.count(), 4)

    # --- Test Book Detail View (GET /api/books/<pk>/) ---

    def test_retrieve_book_unauthenticated(self):
        """
        Ensure unauthenticated users can retrieve a specific book.
        """
        response = self.unauthenticated_client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_retrieve_book_authenticated(self):
        """
        Ensure authenticated users can retrieve a specific book.
        """
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_retrieve_nonexistent_book(self):
        """
        Ensure retrieving a non-existent book returns 404 Not Found.
        """
        response = self.client.get(self.detail_url(9999)) # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # --- Test Book Update View (PUT /api/books/<pk>/update/) ---

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update an existing book (PUT).
        """
        updated_data = {
            'title': 'Updated Book Title',
            'publication_year': 2021,
            'author': self.author2.id # Change author
        }
        response = self.client.put(self.update_url(self.book1.id), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db() # Reload book1 from database to get updated values
        self.assertEqual(self.book1.title, 'Updated Book Title')
        self.assertEqual(self.book1.publication_year, 2021)
        self.assertEqual(self.book1.author, self.author2)

    def test_partial_update_book_authenticated(self):
        """
        Ensure authenticated users can partially update an existing book (PATCH).
        """
        partial_data = {'publication_year': 2023}
        response = self.client.patch(self.update_url(self.book1.id), partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.publication_year, 2023)
        self.assertEqual(self.book1.title, "The First Journey") # Title should remain unchanged

    def test_update_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot update a book.
        """
        updated_data = {
            'title': 'Attempted Update',
            'publication_year': 2021,
            'author': self.author1.id
        }
        response = self.unauthenticated_client.put(self.update_url(self.book1.id), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Verify book data hasn't changed
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Attempted Update')

    def test_update_book_with_future_publication_year(self):
        """
        Ensure updating a book with a future publication year fails validation.
        """
        future_year = date.today().year + 1
        updated_data = {
            'title': self.book1.title,
            'publication_year': future_year,
            'author': self.author1.id
        }
        response = self.client.put(self.update_url(self.book1.id), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
        self.assertEqual(response.data['publication_year'][0], 'Publication year cannot be in the future.')

    def test_update_nonexistent_book(self):
        """
        Ensure updating a non-existent book returns 404 Not Found.
        """
        data = {'title': 'Non Existent', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(self.update_url(9999), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # --- Test Book Delete View (DELETE /api/books/<pk>/delete/) ---

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 3) # One book deleted
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_delete_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot delete a book.
        """
        response = self.unauthenticated_client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 4) # Book should not be deleted
        self.assertTrue(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_nonexistent_book(self):
        """
        Ensure deleting a non-existent book returns 404 Not Found.
        """
        response = self.client.delete(self.delete_url(9999)) # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Book.objects.count(), 4) # No books should be deleted
