from django import forms
from .models import Contacto, Producto

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
    