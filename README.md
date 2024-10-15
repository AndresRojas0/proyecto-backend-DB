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
* cd mi-pagina-de-inicio  
* Ejecuta el archivo app.py

# Instrucciones en PythonAnywhere
* PythonAnywhere -> Web -> Add new web app
* Select a Python Web framework -> Flask
* Select a Python versión -> (la más reciente)
* Quickstart new Flask Project (dejar el path por defecto)

## Consoles -> Bash
``` $ ls ``` ver directorios

``` $ git clone [url del repo] ``` clona el repositorio

``` $ ls ``` ver directorios nuevamente

``` $ exit ``` cerrar consola

## Databases 
* Create a database -> Database name: basedatos
* MySQL password: (crear password alfanumérica)

## Consoles -> Bash
``` mysql> -u AndresRojas -h AndresRojas.mysql.pythonanywhere-services.com -p 'AndresRojas$basedatos' ```

``` mysql> show databases; ```

``` mysql> use AndresRojas$basedatos; ```

``` mysql> source ./proyecto-backend-DB/backup_db/basedatos.sql ```

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