#Define las vistas que existen
from .models import Usuarios
# para todo es import *

from django.template import loader
from django.http import HttpResponse

# Para cargar el template y devolver un httpresponse sin tener que importar ni
# escribir mucho.
from django.shortcuts import render


def index(request):
    # Ejemplo cedula_usuarios: V-1234567
    # TODOS LOS USUARIOS.
    usuarios = Usuarios.objects.all() # Esto trae todos los usuarios de la BD.
    # En esta variable, context, se pasan todas las variables que el template
    # necesita, en nuestro caso, index.html necesita la variable lista_de_usuarios
    # representada como 'lista_de_usuarios' y la info que se le va a pasar está 
    # dentro de la variable lista_de_usuarios.
    context = {
        'lista_de_usuarios': usuarios,
    }
    
    # Manera larga.
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))
    
    # Manera corta.
    # return render(request, 'polls/index.html', context)
    
    # lo_que_se_va_a_mostrar = ",".join([ str(usuario_mostrar) for usuario_mostrar in lista ])
    # return HttpResponse("You're looking at user %s." % lo_que_se_va_a_mostrar ) 
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def cedula(request, cedula_usuarios):
    # Ejemplo cedula_usuarios: V-1234567
    # Para buscar uno por cédula.
    usuario = Usuarios.objects.get(cedula=cedula_usuarios) # Esto busca un usuario en específico, si lo encuentra te lo devuelve, sino, error.
    return HttpResponse("You're looking at user %s." % usuario )
    

def saludos(request, saludos_fer): #cada página que tendré
    return HttpResponse("Vamos a mandarte saludos sin la a :  %s." % saludos_fer)
