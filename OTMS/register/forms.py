from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.CharField(max_length=100)
    other_data = forms.CharField(max_length=256, required=False)


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email", "role", "other_data")

