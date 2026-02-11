from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from user_profile.forms import ProfileForm
from user_profile.models import Profile
from django.contrib.auth import get_user_model

class ProfileFormTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@mail.ru', password='test')
        self.profile = Profile.objects.create(user=self.user, gender='M')

    def test_change_profile(self):
        self.client.login(username=self.user.username, password='test')
        response = self.client.post(reverse('user_profile:index', kwargs={'pk':self.user.id}), data={'gender': 'F'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Profile.objects.filter(user=self.user, gender='F').exists())