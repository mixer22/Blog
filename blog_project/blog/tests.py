import datetime
import time

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Post
from .forms import CommentForm

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Заголовок", content = "контент")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Заголовок")
        self.assertEqual(self.post.content, "контент")

class PostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Заголовок", content="контент")
        self.post = User.objects.create_user(username="testuser", password="pass123")

    def test_post_list_view(self):
        self.client.login(username = "testuser", password="pass123")
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Заголовок")

class CommentFormTest(TestCase):
    def test_valid_form(self):
        data = {"author":"Nik", "content":"123123"}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {"content":"123123"}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())