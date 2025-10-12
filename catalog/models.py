from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание товара')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, db_index=True ,verbose_name='Цена')
    image = models.ImageField(upload_to='catalog', verbose_name='Изображение товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления товара')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления товара')
