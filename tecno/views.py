from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'tecno/index.html')

def contacto(request):
    return render(request,'tecno/contacto.html')

def productos(request):
    return render(request,'tecno/productos.html')

def carrito(request):
    return render(request,'tecno/carrito.html')

def usuario1(request):
    return render(request,'tecno/usuario1.html')

def usuario2(request):
    return render(request,'tecno/usuario2.html')
