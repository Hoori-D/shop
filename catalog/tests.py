from django.test import TestCase

from .models import Plant, Category


class PlantTest(TestCase):
    def test_get_absolute_url(self):
        plant = Plant(name='Test', description='Test description', slug='test', image='test.jpg', price=100)
        self.assertEqual(plant.get_absolut_url(), '/catalog/plant/test/')


class CategoryTest(TestCase):
    def test_get_absolute_url(self):
        category = Category(name='Test', slug='test')
        self.assertEqual(category.get_absolut_url(), '/catalog/test/')