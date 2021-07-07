from django.contrib import admin
from . import models
 
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=("id","categoria_pertenece","title","price")
    list_filter=["categoria_pertenece"]
    ordering=["categoria_pertenece"]

admin.site.register(models.Categorias)
admin.site.register(models.Productos,ProductAdmin)
# admin.site.register(models.Carrito)
