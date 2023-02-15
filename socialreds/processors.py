from .models import Link

def ctx_dict(request):
    ctx={}
    # cargar lista de redes sociales
    links = Link.objects.all()
    #agregar en el diccionario
    for link in links:
        ctx[link.key]=link.url #llenando diccionario
    return ctx 