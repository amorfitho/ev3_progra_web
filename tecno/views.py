from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'tecno/index.html')

def contacto(request):
    return render(request,'tecno/contacto.html')

def productos(request):
    return render(request,'tecno/productos.html')
