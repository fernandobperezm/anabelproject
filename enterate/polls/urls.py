
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<cedula_usuarios>(V\-[0-9]+))/$', views.detail, name='detail'),
    
    url(r'^(?P<saludos_fer>([b-z]+))/$', views.saludos, name='saludos para ti'),
 ]