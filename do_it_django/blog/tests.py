from django.http import response
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

    def test_post_detail(self):
        # if post
        post_001 = Post.objects.create(
            title='First Post',
            content='Hello, World. We are the World.'
        )
        self.assertEqual(Post.objects.count(), 1)

        # post_url == '/blog/1'
        self.assertEqual(post_001.get_absolute_url(), '/blog/1/')

        # response.status_code == 200
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        # navbar
        soup = BeautifulSoup(response.content, 'html.parser')
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('About', navbar.text)

        # post_title in Web Tab Title
        self.assertIn(post_001.title, soup.title)

        # post_title in Post-area
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(post_001.title, post_area.text)

        # post_content in post-area
        self.assertIn(post_001.content, post_area.text)
