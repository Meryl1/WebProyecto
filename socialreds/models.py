from django.db import models


# Create your models here.
class Link(models.Model):
    key= models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name= models.CharField(max_length=200, verbose_name="Red social")
    url= models.URLField(verbose_name="enlace", max_length=200, null=True, blank=True)
    created= models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")  #toma fecha del momento en que se crea         #es necesario agregar estos campos de creacion y actualizacion por buenas practicas
    updated= models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")      #cambia segun las actualizaciones

    class Meta: #modificaciones extendidas del modelo: cambiar nombre, ordenar registros etc
        verbose_name="enlace"
        verbose_name_plural="enlaces"
        ordering=['name'] #- ordena desde el ultimo que se creo hasta el mas antiguo

    def __str__(self): # metodo srt --> retorna en forma de string la informacion del objeto
        return self.name