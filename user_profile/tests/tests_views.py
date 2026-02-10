from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestsViews(TestCase):
    def test_login_user_profile_access(self):
        user = get_user_model().objects.create_user(username='Test', email='', password='test')
        self.client.login(username='Test', password='test')
        response = self.client.get(reverse('user_profile:index', kwargs={'pk': user.id}))
        self.assertEqual(response.status_code, 200)

    def test_not_login_user_profile_access(self):
        response = self.client.get(reverse('user_profile:index', kwargs={'pk': 1}))
        self.assertRedirects(response, f"{reverse('user:login')}?next={reverse('user_profile:index', kwargs={'pk': 1})}")

    def test_login_user_other_profile_access(self):
        user = get_user_model().objects.create_user(username='Test', email='', password='test')
        response = self.client.get(reverse('user_profile:index', kwargs={'pk': 1}))
        self.assertRedirects(response, f"{reverse('user:login')}?next={reverse('user_profile:index', kwargs={'pk': 1})}")