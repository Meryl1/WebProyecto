from django.db import models

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=200, verbose_name="Titulo")
    price=models.FloatField(verbose_name="Precio", null=True)
    price_ant= models.FloatField(verbose_name="Precio anterior", null=True)
    image= models.ImageField(verbose_name="Imagen", upload_to="productos") #en carpeta productos se guarda las imagenes
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")  #toma fecha del momento en que se crea         #es necesario agregar estos campos de creacion y actualizacion por buenas practicas
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")      #cambia segun las actualizaciones


    class Meta: #modificaciones extendidas del modelo: cambiar nombre, ordenar registros etc
        verbose_name="producto"
        verbose_name_plural="productos"
        ordering=["-created"] #- ordena desde el ultimo que se creo hasta el mas antiguo

    def __str__(self): # metodo srt --> retorna en forma de string la informacion del objeto
        return self.title