from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=100)
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput())