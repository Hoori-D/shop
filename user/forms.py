from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Почта', max_length=100, widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'example@example.com',
        }))

    username = forms.CharField(label='Логин', max_length=100, widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'User',
        }))

    password1 = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '********',
        }))

    password2 = forms.CharField(label='Повтор пароля', max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '********',
        }))

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']