from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False, db_index=True, verbose_name='Название')
    description = models.TextField(default='', unique=False, blank=False, null=False, verbose_name='Описание товара')
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False, verbose_name='URL-адрес')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, unique=False, blank=False, null=False, db_index=True ,verbose_name='Цена')
    image = models.ImageField(upload_to='catalog', unique=False, blank=False, null=False, verbose_name='Изображение товара')
