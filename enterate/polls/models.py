from django.db import models

#MODELO DE LA BASE DE DATOS. 
#conjunto de tablas, junto con sus atributos y propiedades. 
#las clases son las tablas
#los atributos son las columnas



# https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models 
# Referencia de todos los tipos.
#migracion: actualizas las bases de datos, la forma o atributos, hasta nombres



class Question(models.Model):     #crea tabla
    question_text = models.CharField(max_length=200) #crea las columnas
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):      #para impresion bonita cuando hago Question.objects.all() en el 
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

#usuarios(cédula, nombre, apellido, teléfono, email, contraseña)
class Usuarios(models.Model):     #crea tabla
    nombre = models.CharField(max_length=20) #crea las columnas
    apellido = models.CharField(max_length=25)
    cedula = models.CharField(max_length=20, primary_key = True) #es char porque no voy a hacer operaciones con ese valor
    telefono = models.CharField(max_length=25)
    email = models.EmailField()
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre + " " +  self.apellido
        
#Estacionamiento(RIF, nombre, Numero_de_puestos)        
class Estacionamiento(models.Model):
    RIF = models.CharField(max_length=20, primary_key = True)
    Nombre = models.CharField(max_length=200)
    Numero_de_puestos = models.IntegerField(default=1000)
    Acceso_restringido = models.BooleanField(default=True)
    
    def __str__(self):
        return self.RIF + " " + self.Nombre
        
#vehiculos(Placa,CEDULA,)   
class Vehiculos(models.Model):
    Cedula = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
    Placa =models.CharField(max_length=20, primary_key = True)
    
    def __str__(self):
        return self.Placa + " " + self.Cedula.__str__()

# alertas(numero,tipo)
class Alertas(models.Model):
    Numero_alertas = models.AutoField(primary_key = True) # Deberiamos quitar esto o cambiarlo a IntegerField porque aunque se borre la BD igual queda el contador.
    Tipo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Numero_alertas.__str__() + " " + self.Tipo 
    
#Ocurre_a(Cedula,numero,fecha)
class Ocurre_a(models.Model):
    Cedula_usuarios_en_alertas = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
    Numero_alertas = models.ForeignKey(Alertas, on_delete=models.CASCADE )
    Fecha_alertas    = models.DateTimeField('fecha de alerta')
    
    def __str__(self):
        return self.Cedula_usuarios_en_alertas.__str__() + " " + self.Numero_alertas.__str__() + " " + self.Fecha_alertas.__str__()
        
#Ocurre_en(RIF,numero,fecha)
class Ocurre_en(models.Model):
    RIF = models.ForeignKey( Estacionamiento, on_delete=models.CASCADE) 
    Numero_alertas = models.ForeignKey( Alertas, on_delete=models.CASCADE)
    Fecha_alertas    = models.DateTimeField('fecha de alerta')
    
    def __str__(self):
        return self.RIF.__str__() + " " + self.Numero_alertas.__str__() + " " + self.Fecha_alertas.__str__()

#Ticket( Placa, RIF,numero,hora_entrada, hora salida)
class Ticket(models.Model):
    Placa = models.ForeignKey(Vehiculos, on_delete=models.CASCADE) 
    RIF = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE)
    Numero_ticket = models.IntegerField(default=0)
    Hora_entrada =  models.DateTimeField('Hora de entrada')
    Hora_salida =  models.DateTimeField('Hora de salida')
    Pagado = models.BooleanField(default=False) # Tiene que añadirse un valor por defecto cuandohay campos booleanos.
    
    def __str__(self):
        return self.Placa.__str__() + " " + self.RIF.__str__() + " " + self.Numero_ticket.__str__() + " " + self.Hora_entrada.__str__() + " " + self.Hora_salida.__str__() + " " + self.Pagado.__str__()

# # GUSTOS(cédula, gusto_entrada, gusto_sal)
# class Gustos(models.Model):
#     cedula = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
#     gusto_entrada = models.CharField(max_length=200)
#     gusto_salida = models.CharField(max_length=200)


