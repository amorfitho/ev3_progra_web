from django.urls import path
from . views import index, contacto, productos,carrito,usuario1,usuario2,agregar_producto,lista_productos


urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('usuario1/', usuario1, name="usuario1"),
    path('usuario2/', usuario2, name="usuario2"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('lista-producto/', lista_productos, name="lista_producto")

]