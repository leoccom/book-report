from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

RESERVED_KEYWORDS = ["update", "delete", "admin", "login", "logout"]

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ["username", "full_name", "email", "password1", "password2"]
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists() or username in RESERVED_KEYWORDS:
            raise forms.ValidationError("Username is already taken or is a reserved keyword. Please choose another.")
        return username

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email"]