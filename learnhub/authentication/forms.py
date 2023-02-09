from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib import messages 


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        widget=forms.PasswordInput, label='confirm password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

  