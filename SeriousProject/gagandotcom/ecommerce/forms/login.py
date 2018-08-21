
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email address', required=True, max_length=100)
    cpatcha=forms.CharField(label='captcha', max_length=10, required=True)
    userpassword = forms.CharField(label='Enter Password', widget=forms.PasswordInput())
