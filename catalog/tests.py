from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Plant, Category


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test', slug='test')

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolut_url(), '/catalog/test/')



class PlantTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test', slug='test')
        self.plant = Plant.objects.create(name='Test', description='Test description', stock_count=20, sale=20, slug='test', image='test.jpg', price=125, category=Category.objects.get(name='Test'))

    def test_negative_sale(self):
        self.plant.sale = -100
        with self.assertRaises(ValidationError):
            self.plant.full_clean()

    def test_gte100_sale(self):
        self.plant.sale = 101
        with self.assertRaises(ValidationError):
            self.plant.full_clean()

    def test_negative_in_stock(self):
        self.plant.stock_count = -100
        with self.assertRaises(ValidationError):
            self.plant.full_clean()

    def test_negative_price(self):
        self.plant.price = -100
        with self.assertRaises(ValidationError):
            self.plant.full_clean()

    def test_get_absolute_url(self):
        self.assertEqual(self.plant.get_absolut_url(), '/catalog/plant/test/')

    def test_get_sale_price(self):
        self.assertEqual(self.plant.get_sale_price(), 100.00)