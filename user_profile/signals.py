from django.contrib.auth import user_logged_in, user_logged_out, get_user_model
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from user_profile.models import Profile


@receiver([post_save, post_delete], sender=Profile)
def user_profile_clear_cache(sender, **kwargs):
    cache.delete_pattern('*profile_page*')


@receiver([post_save, post_delete], sender=get_user_model())
def user_clear_cache(sender, **kwargs):
    cache.delete_pattern('*profile_page*')


@receiver([user_logged_in, user_logged_out])
def login_or_logout_cache_clear(sender, **kwargs):
    cache.delete_pattern('*profile_page*')