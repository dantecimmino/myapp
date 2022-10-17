from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from AppCoder.models import *



class FormRegistro(UserCreationForm):

    email = forms.EmailField(label='Correo')
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class PaletasPadelForm(forms.ModelForm):

    class Meta:

        model = PaletasPadel
        fields= ['nombre','material','marca','forma','precio','imagen']


class PelotasForm(forms.ModelForm):

    class Meta:

        model = Pelotas
        fields= ['marca','precio','imagen']


class AvatarForm(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['user','imagen'] 

