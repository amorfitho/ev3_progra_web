from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

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
@permission_required('tecno.add_producto')
def agregar_producto(request):

    data ={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto registrado")
        else:
            data["form"] = formulario
    
    return render(request,'tecno/producto/agregar.html', data)
#-------------------------------------------------------------------------------------------
@permission_required('tecno.view_producto')
def lista_productos(request):
    productos=Producto.objects.all()
    """""""""""""""
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = Paginator.page(page)
    except:
        raise Http404
    """""""""""""""
    data = {
        'productos': productos
    }

    return render(request,'tecno/producto/lista.html', data)
#-------------------------------------------------------------------------------------------
@permission_required('tecno.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "editado correctamente")
            return redirect(to="lista_producto")
        data["form"] = formulario


    return render(request,'tecno/producto/modificar.html',data)
#-------------------------------------------------------------------------------------------
@permission_required('tecno.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="lista_producto")
#-------------------------------------------------------------------------------------------
@login_required
def cerrar(request):
    logout(request)
    return redirect(to="index")
#-------------------------------------------------------------------------------------------
def registro(request):
    
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Nombre de usuario ya existente")
        else:
            user = User.objects.create_user (username=username, password=password)
            user.save()
            messages.success(request, "Cuenta creada exitosamente")
            return redirect(to="index")
    
    """"""""""
    data = {
        'form': CustomCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomCreationForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro exitoso")
            return redirect(to='index')
        else:
            data["form"]= formulario
    """""""""
    return render(request, 'registration/registro.html')