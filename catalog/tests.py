from django.test import TestCase

from .models import Plant, Category


class PlantTest(TestCase):
    def setUp(self):
        self.plant = Plant(name='Test', description='Test description', sale=5, slug='test', image='test.jpg', price=125)
        self.plant2 = Plant(name='Test2', description='Test description2', sale=38, slug='test', image='test.jpg', price=372)

    def test_get_absolute_url(self):
        self.assertEqual(self.plant.get_absolut_url(), '/catalog/plant/test/')

    def test_get_sale_price(self):
        self.assertEqual(self.plant.get_sale_price(), 118.75)
        self.assertEqual(self.plant2.get_sale_price(), 230.64)


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='Test', slug='test')

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolut_url(), '/catalog/test/')