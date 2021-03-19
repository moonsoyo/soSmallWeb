from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # post list page
        response = self.client.get('/algorithms/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Algorithms')

        navbar = soup.nav

        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id='main_area')
        self.assertIn('No posts yet.', main_area.text)

        post_001 = Post.objects.create(
            title='First post.',
            content='Hello World. We are the world.',
        )

        post_002 = Post.objects.create(
            title='Second post.',
            content='What a nice weather!',
        )

        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/algorithms/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        main_area = soup.find('div', id='main_area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        self.assertNotIn('No posts yet.', main_area.text)