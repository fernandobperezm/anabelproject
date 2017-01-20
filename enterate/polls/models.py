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

# class Usuarios(models.Model):     #crea tabla
#     Nombre = models.CharField(max_length=20) #crea las columnas
#     Apellido = models.CharField(max_length=25)
#     Cedula = models.CharField(max_length=20, primary_key = True) #es char porque no voy a hacer operaciones con ese valor
#     Email = models.EmailField()
    
# class Gustos(models.Model):
#     Mequiere = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
#     #el primer argumento llama a la esa tabla porque no puede existir respuest sin pregunta
#     #el on_delete.cascade cuando se borre a lo que él hacía referencia, eso se borra.
#     Cuanto = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)



