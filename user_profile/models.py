from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDERS = {
        "M": "Мужчина",
        "F": "Женщина",
    }
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(upload_to='user_profile/profile_images/', verbose_name='Изображение профиля')
    gender = models.CharField(blank=True, max_length=1, choices=GENDERS)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

@receiver(post_save,sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

