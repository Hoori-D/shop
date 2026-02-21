from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.core.cache import cache


@receiver([user_logged_in, user_logged_out])
def clear_main_page_on_logout(sender, request, user, **kwargs):
    cache.delete_pattern('*main_page*')


@receiver([user_logged_in, user_logged_out])
def clear_about_page_on_logout(sender, request, user, **kwargs):
    cache.delete_pattern('*about_page*')