from django import forms
from django.contrib.auth import get_user_model

from user_profile.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'gender']