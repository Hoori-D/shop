from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=100, widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com',
            'id': 'email',
            'aria-describedby': 'email-addon',
        }))
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '********',
        }))