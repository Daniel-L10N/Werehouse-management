from django.contrib import admin
from .models import Producto, UnidadMedida, Almacen

admin.site.register(Almacen)
admin.site.register(UnidadMedida)
admin.site.register(Producto)
