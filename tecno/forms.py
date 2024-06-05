from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
#from django.db import 
#from django.contrib.auth.forms import u


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
    
#class LoginForm(auth_user):

    #class Meta:
        #model=

class CustomCreationForm(UserCreationForm):
    
    pass