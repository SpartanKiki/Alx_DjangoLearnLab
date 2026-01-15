from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=2021,
            author=self.author2
        )

        # URLs
        self.list_url = reverse("book-list")
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})

    # ------------------------
    # READ OPERATIONS
    # ------------------------
    def test_list_books_allowed_for_anyone(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # ------------------------
    # CREATE
    # ------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Gamma Book",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated_denied(self):
        data = {
            "title": "Denied Book",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------
    # UPDATE
    # ------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "Updated Title",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_unauthenticated_denied(self):
        data = {
            "title": "Fail Update",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------
    # DELETE
    # ------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_unauthenticated_denied(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------
    # FILTER / SEARCH / ORDER
    # ------------------------
    def test_filter_by_title(self):
        response = self.client.get(self.list_url, {"title": "Alpha Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_by_author_name(self):
        response = self.client.get(self.list_url, {"search": "Author Two"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
