from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm,ProductoForm
# Create your views here.

def index(request):
    return render(request,'tecno/index.html')
#-------------------------------------------------------------------------------------------
def contacto(request):
    data = {
        'form':ContactoForm()
        }
    
    if request.method=='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensage"] = "Enviado"
        else:
            data["form"] = formulario

    return render(request,'tecno/contacto.html', data)
#-------------------------------------------------------------------------------------------
def productos(request):
    productos=Producto.objects.all()
    data = {
        'productos': productos
        }
    return render(request,'tecno/productos.html', data)
#-------------------------------------------------------------------------------------------

def carrito(request):
    return render(request,'tecno/carrito.html')
#-------------------------------------------------------------------------------------------

def usuario1(request):
    return render(request,'tecno/usuario1.html')
#-------------------------------------------------------------------------------------------

def usuario2(request):
    return render(request,'tecno/usuario2.html')
#-------------------------------------------------------------------------------------------
def agregar_producto(request):

    data ={
        'form': ProductoForm()
    }

    

    return render(request,'tecno/producto/agregar.html', data)
