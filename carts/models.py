from django.contrib.auth import get_user_model
from django.db import models

from catalog.models import Plant




class Cart(models.Model):
    user = models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE, related_name='carts', verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания корзины')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


    def __str__(self):
        return f'Корзина пользователя {self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='orders', verbose_name='Корзина')
    plant = models.ForeignKey(to=Plant, on_delete=models.CASCADE, related_name='orders', verbose_name='Растение')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления в корзину')


    class Meta:
        verbose_name = 'Товары в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f'Товар {self.plant} в количестве {self.quantity} шт.'

    def total_price(self):
        return self.plant.price * self.quantity