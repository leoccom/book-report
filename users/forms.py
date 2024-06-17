from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ["username", "full_name", "email", "password1", "password2"]

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]