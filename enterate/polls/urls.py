
from django.conf.urls import url

from . import views

urlpatterns = [
    # LOS parentesis en la expresión (?P<question_id>[0-9]+). que lo que 
    # Django haga match, por ejemplo: 52. Lo pasará como argumento a la vista.
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # ex: /polls/V-1234567
    url(r'^(?P<cedula_usuarios>(V\-[0-9]+))/$', views.cedula, name='cedula'),
    # ex: /polls/<Cualquier palabra sin a y que no esté antes>
    url(r'^(?P<saludos_fer>([b-z]+))/$', views.saludos, name='saludos para ti'),
 ]