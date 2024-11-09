from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']