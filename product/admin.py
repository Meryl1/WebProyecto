from django.contrib import admin
from .models import Product

# Register your models here.
#Clase para configuracion extendida al administrador crearlo con el nombre del modelo + admin
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #solo se visualizan los campos que se especifica, de solo lectura

admin.site.register(Product, ProductAdmin)
