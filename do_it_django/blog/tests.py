from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Category, Post
from django.contrib.auth.models import User

# Create your tests here.


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_tester1 = User.objects.create_user(
            username='tester1',
            password='test',
        )
        self.user_tester2 = User.objects.create_user(
            username='tester2',
            password='test',
        )

        self.category_programming = Category.objects.create(
            name='programming', slug='programming'
        )
        self.category_music = Category.objects.create(
            name='music', slug='music'
        )

        self.post_001 = Post.objects.create(
            title='First Post',
            content='Hello World, We are the World.',
            author=self.user_tester1,
            category=self.category_programming,
        )
        self.post_002 = Post.objects.create(
            title='Second Post',
            content='First is not at all',
            author=self.user_tester2,
            category=self.category_music,
        )
        self.post_003 = Post.objects.create(
            title='Third Post',
            content='Third party',
            author=self.user_tester2,
        )

    def navbar_test(self, soup):
        # NAV Bar
        navbar = soup.nav
        # Nav Bar in Blog, About me
        self.assertIn('Blog', navbar.text)
        self.assertIn('About me', navbar.text)

        logo_btn = navbar.find('a', text="Do It Django")
        self.assertEqual(logo_btn.attrs['href'], '/')

        home_btn = navbar.find('a', text='Home')
        self.assertEqual(home_btn.attrs['href'], '/')

        blog_btn = navbar.find('a', text='Blog')
        self.assertEqual(blog_btn.attrs['href'], '/blog/')

        about_me_btn = navbar.find('a', text='About me')
        self.assertEqual(about_me_btn.attrs['href'], '/about_me/')

    def category_card_test(self, soup):
        categories_card = soup.find('div', id='categories-card')
        self.assertIn('Categories', categories_card.text)
        self.assertIn(
            f'{self.category_programming} ({self.category_programming.post_set.count()})', categories_card.text)
        self.assertIn(
            f'{self.category_music} ({self.category_music.post_set.count()})', categories_card.text)
        self.assertIn(
            f'미분류 ({Post.objects.filter(category=None).count()})', categories_card.text)

    def test_post_list_with_posts(self):
        # if post.count == 3
        self.assertEqual(Post.objects.count(), 3)

        # page Load
        response = self.client.get('/blog/')
        # Page Load Success
        self.assertEqual(response.status_code, 200)
        # HTML parse
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertIn('Blog', soup.title.text)

        self.navbar_test(soup)
        self.category_card_test(soup)

        # page refresh
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')

        main_area = soup.find('div', id='main-area')
        self.assertNotIn('Post is Empty.', main_area.text)

        post_001_card = main_area.find('div', id='post-1')
        self.assertIn(self.post_001.title, post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)

        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)

        post_003_card = main_area.find('div', id='post-3')
        self.assertIn(self.post_003.title, post_003_card.text)
        self.assertIn('미분류', post_003_card.text)

        # not "Post is Empty"
        self.assertIn(self.post_001.author.username.upper(), main_area.text)
        self.assertIn(self.post_002.author.username.upper(), main_area.text)

    def test_post_list_without_posts(self):
        Post.objects.all().delete()

        # Post Empty
        self.assertEqual(Post.objects.count(), 0)

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup)
        self.assertIn('Blog', soup.title.text)

        # "Post is Empty"
        main_area = soup.find('div', id='main-area')
        self.assertIn("Post is Empty.", main_area.text)

    def test_post_detail(self):
        self.assertEqual(Post.objects.count(), 3)

        # post_url == '/blog/1'
        self.assertEqual(self.post_001.get_absolute_url(), '/blog/1/')

        # response.status_code == 200
        response = self.client.get(self.post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        # navbar
        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup)
        self.category_card_test(soup)

        # post_title in Web Tab Title
        self.assertIn(self.post_001.title, soup.title.text)

        # post_title in Post-area
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(self.post_001.title, post_area.text)
        self.assertIn(self.post_001.category.name, post_area.text)

        self.assertIn(self.user_tester1.username.upper(), post_area.text)
        # post_content in post-area
        self.assertIn(self.post_001.content, post_area.text)
