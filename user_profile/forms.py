from django import forms
from django.contrib.auth import get_user_model
from django.forms import TextInput, ModelForm, EmailInput, Select, FileInput

from user_profile.models import Profile


class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','first_name', 'last_name']
        widgets = {
            'username':TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'username'}),
            'email':EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'name@example.com'}),
            'first_name':EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'name'}),
            'last_name':EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'surname'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'gender']
        widgets = {
            'image': FileInput(attrs={'class': 'form-control mb-3', }),
            'gender':Select(attrs={'class': 'form-select mb-3',}),
        }