from flask import jsonify
from flask import render_template
import mysql.connector

from app import app

config_db = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'basedatos'
}

conexion = mysql.connector.connect(**config_db)

@app.route('/api-basedatos/basedatos')
def obtener_personas():

    try:
        cursor = conexion.cursor(dictionary=True)
    except Exception as e:
        print(e)
        print('reconexión')
        conexion.connect()
        cursor = conexion.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM persona;')
    datos = cursor.fetchall()

    return jsonify(datos)

@app.route('/')
def inicio():

    try:
        cursor = conexion.cursor(dictionary=True)
    except Exception as e:
        print(e)
        print('reconexión')
        conexion.connect()
        cursor = conexion.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM persona;')
    datos = cursor.fetchall()

    return render_template('./modelos/personas.html', personas=datos)