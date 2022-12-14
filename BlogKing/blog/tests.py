import datetime
from models import Login
from models import Post
from django.test import TestCase


class PostTestCase(TestCase):
    def setUp(self):
        self.title = 'Test Post'
        self.slug = 'test-post'
        self.author = 'test_user'
        self.content = 'Test Post Content'
        self.status = 0

    def test_post_creation(self):
        post = Post.objects.create(
            title=self.title,
            slug=self.slug,
            author=self.author,
            content=self.content,
            status=self.status
        )

        self.assertEqual(post.title, self.title)
        self.assertEqual(post.slug, self.slug)
        self.assertEqual(post.author, self.author)
        self.assertEqual(post.content, self.content)
        self.assertEqual(post.status, self.status)
        self.assertIsInstance(post.created_on, datetime.datetime)


class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.login_obj = Login.objects.create(
            username=self.username,
            password=self.password
        )

    def test_login_creation(self):
        self.assertEqual(self.login_obj.username, self.username)
        self.assertEqual(self.login_obj.password, self.password)

# Create your tests here.
