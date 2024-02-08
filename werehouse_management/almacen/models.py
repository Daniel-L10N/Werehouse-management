from django.db import models

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=20, blank= True, null= False)
    simbolo = models.CharField(max_length=5, blank= True, null= False)
    def __str__(self):
        return self.simbolo
    
class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion
    