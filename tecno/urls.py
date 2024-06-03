from django.urls import path
from . views import index, contacto, productos


urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('productos/', productos, name="productos"),
]