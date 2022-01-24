from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # page Load
        response = self.client.get('/blog/')
        # Page Load Success
        self.assertEqual(response.status_code, 200)
        # HTML parse
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('Blog', soup.title.text)
        # NAV Bar
        navbar = soup.nav
        # Nav Bar in Blog, About me
        self.assertIn('Blog', navbar.text)
        self.assertIn('About me', navbar.text)

        # Post Empty
        self.assertEqual(Post.objects.count(), 0)

        # "Post is Empty"
        main_area = soup.find('div', id='main-area')
        self.assertIn("Post is Empty.", main_area.text)

        # if post.count == 2
        post_001 = Post.objects.create(
            title='First Post',
            content='Hello World, We are the World.',
        )
        post_002 = Post.objects.create(
            title='Second Post',
            content='First is not at all',
        )
        self.assertEqual(Post.objects.count(), 2)

        # page refresh
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')

        # main-area > post > title. count == 2
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        # not "Post is Empty"
        self.assertNotIn('Post is Empty.', main_area.text)
