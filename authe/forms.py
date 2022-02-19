from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class signup(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields= ['username', 'password1', 'password2']