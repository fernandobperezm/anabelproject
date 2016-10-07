# Pasos para instalar el proyecto localmente en Linux.

## 1- Instalar Python3 desde la página https://www.python.org/downloads/.
## 2- Verificar que PIP esté instalado ejecutando en terminal pip3
## 3- Instalar virtualenv ejecutando en terminal: pip3 install virtualenv 
## 4- Crear el ambiente virtual ejecutando: virtualenv $Dir. Donde $Dir es 
## el directorio donde se encuentra le proyecto.
## 5- Ejecutar el comando: source bin/activate
## 6- Ejecutar: pip3 install django
## 7- Ejecutar: sudo pip3 install psycopg2

### Siempre se puede verificar que django está instalado: python -m django --version

### Si el proyecto no está creado: 
### 1- Ejecutar: django-admin startproject $NombreProyecto.

# El proyecto se corre: python manage.py runserver IP:Puerto

