from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name']


class UserEditForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password']
