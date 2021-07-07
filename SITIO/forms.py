from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields=('username','email','password1','password2')


class ProductsForm(forms.ModelForm):
    class Meta:
        model= models.Productos
        fields=("title","image","description","price","categoria_pertenece")

