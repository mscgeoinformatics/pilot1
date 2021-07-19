from user_app import models
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=models.UserProfileInfo
        fields = ('portfolio_site','profile_picture')
