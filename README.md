# proyecto-backend-DB
Es una práctica de una clase de Fullstack 
[Python Fullstack - Clase adicional](https://www.youtube.com/watch?v=9CS_clxSn0E)

# Descripción del Proyecto
proyecto-backend-DB es una aplicación python que permite ejecutar tu propia API 
en Python para aplicaciones web.

# Instrucciones de Uso
Clona este repositorio en tu host.

# bash
* git clone https://github.com/AndresRojas0/proyecto-backend-DB
* Navega hasta el directorio del proyecto.
* cd directorio-del-proyecto

# Instrucciones en Local host
* `/> python -m venv mientorno` crear entorno
* `/> .\mientorno\Scripts\activate` activar entorno
* `(mientorno) /> pip install -r dependencias.txt` instalar dependencias
* `(mientorno) /> pip install mysql-connector-python` instalar mysql-connector-python
* `(mientorno) /> pip intall flask` instalar flask
* `(mientorno) /> pip install flask-cors` instalar flask-cors
* `(mientorno) /> pip freeze > dependencias.txt` guardar detalle dependencias
 
# Instrucciones en PythonAnywhere (host)
* PythonAnywhere -> Web -> Add new web app
* Select a Python Web framework -> Flask
* Select a Python versión -> (la más reciente)
* Quickstart new Flask Project (dejar el path por defecto)

## PythonAnywhere -> Consoles -> Bash
`$ ls` ver directorios

`$ git clone [url del repo]` clona el repositorio

`$ ls` ver directorios nuevamente

`$ exit` cerrar consola

## PythonAnywhere -> Databases 
* Create a database -> Database name: basedatos
* MySQL password: (crear password alfanumérica)

## PythonAnywhere -> Consoles -> Bash
`mysql> -u AndresRojas -h AndresRojas.mysql.pythonanywhere-services.com -p 'AndresRojas$basedatos'`

`mysql> show databases;`

`mysql> use AndresRojas$basedatos;`

`mysql> source ./proyecto-backend-DB/backup_db/basedatos.sql`

# Despliegue
El proyecto se encuentra desplegado en https://proyecto-backend-db-andresrojas.pythonanywhere.com/

# Funcionalidades
* Acceder a los endpoints API.

# Tecnologías Utilizadas
[![Languages](https://skillicons.dev/icons?i=python,mysql)](https://skillicons.dev)

# Autores
Este proyecto fue desarrollado por Andrés Rojas.

# Licencia
Este proyecto está bajo la licencia MIT.