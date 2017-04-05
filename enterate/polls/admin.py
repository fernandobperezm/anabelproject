#añadir cosas a la pagina web desde la base de datos. 

from django.contrib import admin

# Register your models here.
from .models import Usuarios #lo importa al archivo admin.py
from .models import Estacionamiento
from .models import Vehiculos

# For poll app.
from .models import Question
from .models import Choice

#para ponerlo en la BD
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Usuarios)
admin.site.register(Estacionamiento)
admin.site.register(Vehiculos)
