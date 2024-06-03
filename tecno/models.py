from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=(50))
        
    def _str_(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=(50))
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabri = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def _str_(self):
        return self.nombre
    
