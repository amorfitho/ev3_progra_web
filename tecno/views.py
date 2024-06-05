from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
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

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensage"] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request,'tecno/producto/agregar.html', data)
#-------------------------------------------------------------------------------------------
def lista_productos(request):
    productos=Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request,'tecno/producto/lista.html', data)
#-------------------------------------------------------------------------------------------
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="lista_producto")
        data["form"] = formulario


    return render(request,'tecno/producto/modificar.html',data)
#-------------------------------------------------------------------------------------------
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="lista_producto")