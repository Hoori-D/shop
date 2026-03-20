from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase

from catalog.models import Category

from django.urls import reverse


class TestAboutPage(SimpleTestCase):

    def test_about_page_content(self):
        response = self.client.get(reverse('main:about'))
        self.assertContains(response, 'О нас', status_code=200)


class TestMainPage(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category1', slug='test-category1', image='test.jpg')
        Category.objects.create(name='Test Category2', slug='test-category2', image='test.jpg')

    def test_main_page_context(self):
        response = self.client.get(reverse('main:index'))
        self.assertIn('title', response.context)
        self.assertEqual(response.context['title'], 'Главная страница')
        self.assertIn('slug', response.context)
        self.assertEqual(response.context['slug'], 'all')
        self.assertEqual(len(response.context['categories']), 2)
        self.assertContains(response, 'Test Category1')
        self.assertContains(response, 'Test Category2')