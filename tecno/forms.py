from typing import Any
from django import forms
from .models import Contacto, Producto, Marca
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError



class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto 
        fields = ["nombre","email","tipo_consulta","mensage","avisos"]

class ProductoForm(forms.ModelForm):
    
        #nombre = forms.CharField(min_length=3, max_length=50)
        #precio = forms.IntegerField(min_value=1, max_value=3000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
    
        return nombre

    class Meta:
        model = Producto 
        fields = '__all__'

        widgets = {
            "fecha_fabri": forms.SelectDateWidget()
        }
      

class CustomCreationForm(UserCreationForm):

    password= forms.CharField(min_length=8)
    

    def clean_name(self):
        name = self.cleaned_data["username"]
        existe = User.objects.filter(name__iexact=name).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
    
        return name

    
    class Meta:
        model = User
        fields = ['username',"password"]