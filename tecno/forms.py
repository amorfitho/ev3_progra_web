from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto 
        fields = ["nombre","email","tipo_consulta","mensage","avisos"]

class ProductoForm(forms.ModelForm):
        
    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            "fecha_fabri": forms.SelectDateWidget()
        }
      

class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','direccion',"password"]