from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from catalog.models import Plant, Category


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test', slug='test')

    def test_get_absolute_url(self):
        self.assertEqual(self.category.get_absolut_url(), '/catalogs/test/')



class PlantTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Test', slug='test')

    def setUp(self):
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
        self.assertEqual(self.plant.get_absolut_url(), '/catalogs/plant/test/')

    def test_negative_price_constraints(self):
        self.plant.price = -100.00
        with self.assertRaises(IntegrityError):
            self.plant.save()

    def test_zero_price_constraints(self):
        self.plant.price = 0
        with self.assertRaises(IntegrityError):
            self.plant.save()

    def test_negative_sale_constraints(self):
        self.plant.sale = -20
        with self.assertRaises(IntegrityError):
            self.plant.save()

    def test_gt100_sale_constraints(self):
        self.plant.sale = 120
        with self.assertRaises(IntegrityError):
            self.plant.save()

    def test_negative_stock_count_constraints(self):
        self.plant.stock_count = -55
        with self.assertRaises(IntegrityError):
            self.plant.save()
