from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class signup(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields= ['username','email', 'password1', 'password2']

class changingPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'type':'password'}))
    class Meta:
        model = User
        # fields = '__all__'
        fields= ['old_password','new_password1', 'new_password2']