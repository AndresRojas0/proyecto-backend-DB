# proyecto-backend-DB
Es una práctica de una clase de Fullstack 
[Python Fullstack - Clase adicional](https://www.youtube.com/watch?v=9CS_clxSn0E)

# Descripción del Proyecto
proyecto-backend-DB es una aplicación python que permite ejecutar tu propia API en Python para aplicaciones web.

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

## Crea aplicación web y selecciona el framework: 
* PythonAnywhere -> Web -> Add new web app
* Select a Python Web framework -> Flask
* Select a Python versión -> (la más reciente)
* Quickstart new Flask Project (dejar el path por defecto)

## Clona repositorio desde consola bash: 
* PythonAnywhere -> Consoles -> Bash
`$ ls` ver directorios
`$ git clone [url del repo]` clona el repositorio
`$ ls` ver directorios nuevamente
`$ exit` cerrar consola

## Crea base de datos, selecciona base de datos creada y crea tablas desde script:  
* PythonAnywhere -> Databases -> Create a database

* PythonAnywhere -> Consoles -> Bash
`mysql> -u [USERNAME] -h [USERNAME].mysql.pythonanywhere-services.com -p '[USERNAME]$basedatos'`
`mysql> show databases;`
`mysql> use [USERNAME]$basedatos;`
`mysql> source ./proyecto-backend-DB/backup_db/basedatos.sql`

## Crea base de datos y tablas desde consola MySQL: 
* PythonAnywhere -> Consoles -> MySQL
`CREATE DATABASE basedatos;`
`USE basedatos;`
`CREATE TABLE persona (id INT AUTO_INCREMENT, nombre VARCHAR(50), apellido VARCHAR(50), fecha_nac DATE, doc_identidad VARCHAR(11) UNIQUE NOT NULL, PRIMARY KEY (id));`
`INSERT INTO persona (nombre, apellido, fecha_nac, doc_identidad) 
VALUES ("Albano", "Ablanco", "1980-01-01", "20111222"),("Beny", "Benassi", "1985-01-01", "30111222"),("Catalina", "Cantimplora", "1985-01-01", "35111222"),("Zedd", "Zanahoria", "1999-01-01", "50111222");`

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
