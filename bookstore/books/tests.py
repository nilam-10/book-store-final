from django.test import TestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Author", price=10.00, stock=5)
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.admin = User.objects.create_superuser(username="admin", password="adminpass")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")

    def test_add_to_cart(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse('add_to_cart', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(self.book.id), self.client.session['cart'])

    def test_admin_panel_access(self):
        self.client.login(username="admin", password="adminpass")
        response = self.client.get(reverse('admin_panel'))
        self.assertEqual(response.status_code, 200)