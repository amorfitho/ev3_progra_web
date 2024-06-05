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
    

""""""""""
Class ingresaForm(User):
    
    class Meta:
    model = User
    fields = [username, password]
"""""""""    

class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email", "password1","password2"]