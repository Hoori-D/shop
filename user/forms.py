from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput


class LoginForm(AuthenticationForm):
    username = forms.CharField()

    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    username = forms.CharField()

    password1 = forms.CharField()

    password2 = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']