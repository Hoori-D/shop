from django.test import TestCase

from .models import Plant


class PlantTest(TestCase):
    def test_get_absolute_url(self):
        plant = Plant(name='Test', description='Test description', slug='test', image='test.jpg', price=100)
        self.assertEqual(plant.get_absolut_url(), '/catalog/plant/test/')