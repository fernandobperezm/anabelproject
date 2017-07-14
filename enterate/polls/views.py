#Define las vistas que existen

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def cedula(request, cedula_usuarios):
    return HttpResponse("You're looking at user %s." % cedula_usuarios)    

def saludos(request, saludos_fer): #cada página que tendré
    return HttpResponse("Vamos a mandarte saludos sin la a :  %s." % saludos_fer)
