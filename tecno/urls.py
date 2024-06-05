from django.urls import path
from . views import index, contacto, productos,carrito,usuario1,usuario2,agregar_producto,lista_productos, modificar_producto, eliminar_producto, registro


urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('lista-producto/', lista_productos, name="lista_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/',registro,name="registro"),
]