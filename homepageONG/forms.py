from django import forms
from .models import Imagem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['titulo', 'imagem']

class CriacaoSuperUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        # Marca o usuário como superusuário
        user.is_superuser = True
        user.is_staff = True  # Para permitir o acesso ao admin
        if commit:
            user.save()
        return user