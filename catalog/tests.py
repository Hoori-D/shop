from django.test import TestCase

from .models import Plant, Category


class PlantTest(TestCase):
    def setUp(self):
        self.plant = Plant(name='Test', description='Test description', slug='test', image='test.jpg', price=100)

    def test_get_absolute_url(self):
        self.assertEqual(self.plant.get_absolut_url(), '/catalog/plant/test/')


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='Test', slug='test')

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolut_url(), '/catalog/test/')