from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from slugify import slugify


class Plant(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание товара')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00, 'Цена не может быть меньше 0')], db_index=True ,verbose_name='Цена')
    sale = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0.00, 'Скидка не может быть меньше 0'), MaxValueValidator(100.00, 'Скидка не может быть больше 100')],verbose_name='Скидка в процентах')
    stock_count = models.IntegerField(default=0, validators=[MinValueValidator(0, 'Количество товара не может быть меньше 0')], verbose_name='Количество товара')
    image = models.ImageField(upload_to='catalog/plants', verbose_name='Количество посещений')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Популярность товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления товара')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления товара')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories')

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.stock_count > 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))

        super().save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('catalog:plant_by_slug', kwargs={'slug': self.slug})

    def get_sale_price(self):
        finale_price = self.price - (self.price * self.sale / 100)
        return finale_price




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес')
    image = models.ImageField(upload_to='catalog/categories',
                              verbose_name='Изображение категории')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))

        super().save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('catalog:category_by_slug', kwargs={'slug': self.slug})

