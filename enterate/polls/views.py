#Define las vistas que existen

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index2.")
    
def detail(request, cedula_usuarios):
    return HttpResponse("You're looking at user %s." % cedula_usuarios)    

def saludos(request, saludos_fer): #cada página que tendré
    return HttpResponse("Vamos a mandarte saludos sin la a :  %s." % saludos_fer)
