from django.db import models
from django.urls import reverse

from slugify import slugify


class Plant(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание товара')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, db_index=True ,verbose_name='Цена')
    image = models.ImageField(upload_to='catalog/plants', verbose_name='Изображение товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления товара')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления товара')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=3, related_name='categories')

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.name))

        super().save(*args, **kwargs)

    def get_absolut_url(self):
        return reverse('catalog:plant_by_slug', kwargs={'slug': self.slug})




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

