from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Message
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    username = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2.8,  
            'cols': 37,  
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email','avathar')

