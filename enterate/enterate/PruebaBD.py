#Prueba BD.
# Instrucciones para ejecutar esta prueba. 
# NOTA: esta prueba contiene hasta el momento SOLO inserciones en las tablas de
#       la BD, incluye solamente una fila por cada tabla. También se encarga de 
#       borrar todo lo que esté en todas las tablas para que solo haya que copiarlo
#       y pegarlo.
# PARA CORRERLO: 
#  1- Ejecutar: cd ~/workspace/enterate 
#  2- Ejecutar: python3 manage.py shell
#  3- Copiar y pegar todo el archivo en el terminal.


from polls.models import *
from django.utils import timezone

# Esto borra todo el contenido de cada tabla antes de hacer las inserciones (por si se quiere correr este script varias veces sin preocuparse)
# Sin embargo, esto no reinicia los contadores.
Usuarios.objects.all().delete()
Estacionamiento.objects.all().delete()
Vehiculos.objects.all().delete()
Alertas.objects.all().delete()
Ocurre_a.objects.all().delete()
Ocurre_en.objects.all().delete()
Ticket.objects.all().delete()

# class Usuarios(models.Model):     #crea tabla
#     nombre = models.CharField(max_length=20) #crea las columnas
#     apellido = models.CharField(max_length=25)
#     cedula = models.CharField(max_length=20, primary_key = True) #es char porque no voy a hacer operaciones con ese valor
#     telefono = models.CharField(max_length=25)
#     email = models.EmailField()
#     contrasena = models.CharField(max_length=20)
user1 = Usuarios(
            nombre = "Esteban", 
            apellido = "Quito", 
            cedula="V-22244555", 
            telefono="+58414222555", 
            email="quito.esteban@gmail.com", 
            contrasena="contraseña")
            
user1.save()

# class Estacionamiento(models.Model):
#     RIF = models.CharField(max_length=20, primary_key = True)
#     Nombre = models.CharField(max_length=200)
#     Numero_de_puestos = models.IntegerField(default=1000)
#     Acceso_restringido = models.BooleanField(default=True)
estacionamiento1 = Estacionamiento(
                        RIF = "J-09087854-0",
                        Nombre = "Estacionamiento Centro Comercial Los Caracas",
                        Numero_de_puestos = 187,
                        Acceso_restringido = True)

estacionamiento1.save()

# #vehiculos(placa,CEDULA,)   
# class Vehiculos(models.Model):
#     Cedula = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
#     Placa =models.CharField(max_length=20, primary_key = True)
veh1 = Vehiculos(
            Cedula = user1,
            Placa = "AE339GF")

veh1.save()

# # alertas(numero,tipo)
# class Alertas(models.Model):
#     numero_alertas = models.AutoField(primary_key = True) 
#     tipo = models.CharField(max_length=200)
alerta1 = Alertas(Tipo = "Alerta de Incendio de Vehículo.")
alerta1.save()

# #Ocurre_a(Cedula,numero,fecha)
# class Ocurre_a(models.Model):
#     Cedula_usuarios_en_alertas = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
#     Numero_alertas = models.ForeignKey(Alertas, on_delete=models.CASCADE )
#     Fecha_alertas    = models.DateTimeField('fecha de alerta')
ocurre_a1 = Ocurre_a(
                Cedula_usuarios_en_alertas = user1,
                Numero_alertas = alerta1,
                Fecha_alertas = timezone.now())
ocurre_a1.save()

# #Ocurre_en(RIF,numero,fecha)
# class Ocurre_en(models.Model):
#     RIF = models.ForeignKey( Estacionamiento, on_delete=models.CASCADE) 
#     Numero_alertas = models.ForeignKey( Alertas, on_delete=models.CASCADE)
#     Fecha_alertas    = models.DateTimeField('fecha de alerta')
    
ocurre_en1 = Ocurre_en(
                RIF = estacionamiento1,
                Numero_alertas = alerta1,
                Fecha_alertas = timezone.now())
ocurre_en1.save()

# #Ticket( placa, RIF,numero,hora_entrada, hora salida)
# class Ticket(models.Model):
#     Placa = models.ForeignKey(Vehiculos, on_delete=models.CASCADE) 
#     RIF = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
#     Numero_ticket = models.IntegerField(default=0)
#     Hora_entrada =  models.DateTimeField('Hora de entrada')
#     Hora_salida =  models.DateTimeField('Hora de salida')
#     Pagado = models.BooleanField(default=False)

ticket1 = Ticket(
            Placa = veh1,
            RIF = estacionamiento1,
            Numero_ticket = 0,
            Hora_entrada = timezone.now(),
            Hora_salida = timezone.now(),
            Pagado = True)
ticket1.save()


# Ver si todos se imprimen bien
user1
estacionamiento1
veh1
alerta1
ocurre_a1
ocurre_en1
ticket1